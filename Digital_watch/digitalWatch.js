setInterval(function digital(){
    var time = new Date();
    var seconds = time.getSeconds();
    var minutes = time.getMinutes();
    var hours = time.getHours();
    document.getElementsByClassName('clock')[0].innerHTML = hours + ":" + minutes + ":" + seconds;

    if(hours < 10 && minutes >= 10 && seconds >= 10){
       document.getElementsByClassName('clock')[0].innerHTML = "0" +hours + ":" + minutes + ":" + seconds;
    }
    else if(minutes < 10 && seconds >= 10 && hours >= 10){
       document.getElementsByClassName('clock')[0].innerHTML = hours + ":0" + minutes + ":" + seconds;
    }
    else if(minutes >= 10 && seconds >= 10 && hours >= 10){
        document.getElementsByClassName('clock')[0].innerHTML = hours + ":" + minutes + ":" + seconds;
     }
    else if(seconds < 10 && minutes >= 10 && hours >= 10){
       document.getElementsByClassName('clock')[0].innerHTML = hours + ":" + minutes + ":0" + seconds;
    }
    else if(hours < 10 && minutes < 10 && seconds > 10){
       document.getElementsByClassName('clock')[0].innerHTML = "0" + hours + "0:" + minutes + ":" + seconds;
    }
    else if(hours < 10 && seconds < 10 && minutes > 10){
       document.getElementsByClassName('clock')[0].innerHTML = "0" + hours + ":" + minutes + ":0" + seconds;
    }
    else if(minutes < 10 && seconds < 10 && hours > 10){
       document.getElementsByClassName('clock')[0].innerHTML = hours + ":0" + minutes + ":0" + seconds;
    }
    else if(0 < minutes <10 && 0 < seconds <10 && 0 < hours < 10 ){
       document.getElementsByClassName('clock')[0].innerHTML = "0" + hours + ":0" + minutes + ":0" + seconds;
    }
    else if(minutes == 0 && seconds == 0 && hours == 0 ){
       document.getElementsByClassName('clock')[0].innerHTML = "0" + hours + ":0" + minutes + ":0" + seconds;
    }
},1000)



