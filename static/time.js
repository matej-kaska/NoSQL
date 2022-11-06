setInterval(function(){
    const clock = document.querySelector(".display");
    let time = new Date();
    let sec = time.getSeconds();
    let min = time.getMinutes();
    let hr = time.getHours();

    if (sec < 10) {
        sec = "0" + sec;
    }

    clock.textContent = hr + ':' + min + ':' + sec;});