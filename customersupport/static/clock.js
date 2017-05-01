var $hOut = $('#hours'),
    $mOut = $('#minutes'),
    $sOut = $('#seconds'),
    $ampmOut = $('#ampm');

function update(){
  var date = new Date();

  var ampm = date.getHours() < 12
             ? 'AM'
             : 'PM';

  var hours = date.getHours() == 0
              ? 12
              : date.getHours() > 12
                ? date.getHours() - 12
                : date.getHours();

  var minutes = date.getMinutes() < 10
                ? '0' + date.getMinutes()
                : date.getMinutes();

  var seconds = date.getSeconds() < 10
                ? '0' + date.getSeconds()
                : date.getSeconds();

  $hOut.text(hours + ":");
  $mOut.text(minutes + ":");
  $sOut.text(seconds);
  $ampmOut.text(ampm);
}

update();
window.setInterval(update, 1000);
