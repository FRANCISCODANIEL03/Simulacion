const btn_met = document.getElementById("btn-met")
const btn_view = document.getElementById("btn-view")
const div_imgs = document.getElementById("div_imgs")
const div_tbl = document.getElementById("div_tbl")
const tbl = document.getElementById("tbl-body")
const div_main = document.getElementById("div_main")

URL = "https://model-final.onrender.com/metrics"
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

const limpiarTabla = ()=>{
    while(tbl.firstChild){
        tbl.removeChild(tbl.firstChild)
    }
}
const extraerDat = async ()=>{
    const data = await fetch(URL)
    const dataP = await data.json()
    console.log(dataP)
    limpiarTabla()
    for(let i = 0; i < dataP.length; i++){
        var tr = document.createElement("tr")
        var td1 = document.createElement("td")
        var td2 = document.createElement("td")
        td1.textContent = dataP[i].name
        td2.textContent = (dataP[i].porcent).toFixed(4)
        tr.appendChild(td1)
        tr.appendChild(td2)
        tbl.appendChild(tr)
    }
}




