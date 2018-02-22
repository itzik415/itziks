
var colorChange = function () {
    let upperColor = document.querySelector('.leftColor').value;
    let downColor = document.querySelector('.rightColor').value;
    let rgbName = document.querySelector('h3');
    document.querySelector('body').style.background = `linear-gradient(${upperColor}, ${downColor})`;
    rgbName.textContent = `Upper color: ${upperColor}    ||    Down color: ${downColor}`

}

document.addEventListener('change', colorChange);
