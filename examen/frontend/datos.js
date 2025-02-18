const btn_met = document.getElementById("btn-met")
const btn_view = document.getElementById("btn-view")
const div_imgs = document.getElementById("div_imgs")
const div_tbl = document.getElementById("div_tbl")
const tbl = document.getElementById("tbl-body")
const div_main = document.getElementById("div_main")

URL = "http://localhost:5000/metrics2"
btn_met.addEventListener('click', async (e)=>{
    e.preventDefault()
    extraerDat()
    div_tbl.style.display = 'flex'
    div_main.classList.add("dvs")
    div_main.classList.remove("dvs3")
})

btn_view.addEventListener('click', (e)=>{
    e.preventDefault()
    div_imgs.style.display = 'flex'
})
