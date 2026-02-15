const smallImg = document.querySelectorAll(".gallery img")
const fullImg = document.querySelector(".full-image")
const modal = document.querySelector(".modal")
smallImg.forEach(img=>{
    img.addEventListener("click",()=>{
        fullImg.src = img.src
        modal.classList.add("open")
    })
})

modal.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.classList.remove("open")
    }
})
