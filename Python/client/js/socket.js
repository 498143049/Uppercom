
<script type="text/javascript" charset="utf-8">
    var socket = io.connect('http://127.0.0.1:80');
    socket.on('connect', function() {
         console.log('Time Start');
    });
    socket.on('SendData', function(data) {
    	  var myDate = new Date();
          console.log(data);
          console.log(myDate.getSeconds());
    });
</script>