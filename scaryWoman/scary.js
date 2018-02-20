

document.getElementById("music").play();

document.getElementById("main-opening").addEventListener("click",function() {
    document.getElementById('open').style.display = "none";
    document.getElementById('death').play()
    document.getElementById('horror').style.display = "block";
    document.getElementById("music").pause();
});