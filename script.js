async function getStory() {

    try {

        const response = await fetch("http://127.0.0.1:5000/story");

        const data = await response.json();

        document.getElementById("title").innerText =
            data.title;

        document.getElementById("story").innerText =
            data.story;

    }

    catch(error){

        console.log(error);

        document.getElementById("story").innerText =
            "Backend connection error";

    }

}
