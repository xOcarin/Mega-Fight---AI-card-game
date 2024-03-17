
console.log("connected script")
function changeText(){
    console.log("changing text...");
    fetch('/change_text')
    .then(response => response.json())
    .then(data => {
        document.getElementById('subj1').innerText = data.text1;
        document.getElementById('ab1').innerText = data.text2;
        document.getElementById('subj2').innerText = data.text3;
        document.getElementById('ab2').innerText = data.text4;
    })
    .catch(error => console.error('Error:', error));
}

function genImg(){
    console.log("generating image");
    var imgElement = document.getElementById('fightLink');
    imgElement.src = "/static/placeholderimg.png";

    fetch('/gen_image')
    .then(response => response.json())
    .then(data => {
        document.getElementById('fightLink').src = data.url;
    })
    .catch(error => console.error('Error:', error));


}


document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("nextbtn").addEventListener("click", changeText);
            document.getElementById("nextbtn").addEventListener("click", genImg);
        });