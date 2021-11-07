

const displayTopBarMenu = () =>{
    let topBarMenuId = document.getElementById("topBarMenu").style;
    if(topBarMenuId.display === "none"){
        document.getElementById("topBarMenu").style.display = "grid";
    }else{
        document.getElementById("topBarMenu").style.display = "none";
    }
}