// Modified from: https://codepen.io/seanfree/pen/NrRrvZ

function update() {
    let date = new Date();

    let ampm = date.getHours() < 12
        ? 'AM'
        : 'PM';

    let hours = date.getHours() === 0
        ? 12
        : date.getHours() > 12
            ? date.getHours() - 12
            : date.getHours();

    let minutes = date.getMinutes() < 10
        ? '0' + date.getMinutes()
        : date.getMinutes();

    let seconds = date.getSeconds() < 10
        ? '0' + date.getSeconds()
        : date.getSeconds();

    $('#hours').text(hours + ":");
    $('#minutes').text(minutes + ":");
    $('#seconds').text(seconds);
    $('#ampm').text(ampm);
}

update();
window.setInterval(update, 1000);
