   //有一个定时器，进行数据刷新。数据刷新频率一定。另一个定时器进行数据产生，这个是由webscoket决定的。
      (function () {
        var
          container = document.getElementById('container'),
          data, graph, offset, dataCount,status;
        // Draw a sine curve at time t
        $("#container").height(500);
        // Instantiate a slider
         dataALL = [];
         data=[]
         dataCount=0;
         //数据产生数组
        function reciverData(dataone){
          dataALL.push([dataCount, dataone]) ;           //插入到2个数据中
            var len= data.push([dataCount, dataone]);     //插入到2个数据中，并保持其个数
            if(len>200)
            {
              data.shift();
            }
          dataCount+=0.01;                                     
        };
    // var socket = io.connect('http://127.0.0.1:80/');
     var socket = io.connect('http://192.168.1.100:80/');
     // var socket = io.connect('http://qq498143049.imwork.net/');
      socket.on('connect', function() {
        console.log('ok');
        socket.emit('my event', { my: 'data' });
     });
      socket.on('news', function (data) {
      console.log(data);
      reciverData(data.data);
    });
        var config={
             selection : {
            mode : 'x'
        },
            HtmlText:false,
             yaxis : {
               max : 5,
               min : 0
             }
           }
        //绘图函数
        function Draw () {
          // Draw Graph
          if(status)
          {
           graph = Flotr.draw(container, [ dataALL ], config)
          }
          else
          {
            graph = Flotr.draw(container, [ data ], config)
          }
        };
        //产生定时函数
         // window.setInterval(function () {
         //  reciverData(Math.random());             //接收到的数据);
         //  }, 40);
        //定时绘图函数 
         var Timer = window.setInterval(function () {
            Draw();
          }, 40); //25帧
        //绑定停止开始按键按键
        var change=document.getElementsByClassName("Lbutton")[0];
        change.onclick= function(){
          status=~status;
          if(status)
          {
            change.innerText="    开始   ";
            window.setTimeout(function () {window.clearInterval(Timer);},40);
          }
          else
          {
              change.innerText="   停止   ";
              Timer = window.setInterval(function () {
                Draw();
               }, 40); //25帧
          }
        };
        //基础装饰器
        function drawGraph (opts) {
        // Clone the options, so the 'options' variable always keeps intact.
        o = Flotr._.extend(Flotr._.clone(config), opts || {});
         // Return a new graph.
        return Flotr.draw(container,[ dataALL ],o);
  }
        //时间观察器
         Flotr.EventAdapter.observe(container, 'flotr:select', function(area){
          // Draw selected area
           graph = drawGraph({
           xaxis : { min : area.x1, max : area.x2 },
           yaxis : { min : area.y1, max : area.y2 }
          });
      });
         Flotr.EventAdapter.observe(container, 'flotr:click', function () { graph = drawGraph(); });
      })();