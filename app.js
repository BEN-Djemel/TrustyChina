let sellers = [];

fetch("sellers copy.json")
    .then(res => res.json())
    .then(data => {
        sellers = data;
        renderTable(sellers);
    });
// add la condition en dessous de seller.name : ${seller.verified ? "✅" : "⚠️" : "empty"}

function renderTable(data) {
    const table = document.getElementById("sellerTable");
    table.innerHTML = "";
    let compteur = 0;
    data.forEach(seller => {
        compteur = compteur+1
        const row = document.createElement("tr");
        row.innerHTML = `
            <td width="3%">${compteur}</td>
            <td width="12%">${seller.type}</td>
            <td width="12%">${seller.name}</td>
            <td width="12%"><a href="${seller.catalog_url}" target="_blank">${seller.catalog_type}</a></td>
            <td width="12%"><a href="${seller.catalog_url2}" target="_blank">${seller.catalog_type2}</a></td>
            <td width="10%">${seller.known_for}</td>
            <td width="7%">${seller.quality_rating}</td>
            <td width="7%">${seller.price_rating}</td>
            <td width="17%">${seller.description}</td>
            <td width="100px">
            ${seller.contact_type.toLowerCase() === "whatsapp" ? "<img width='20px' height='20px' src='https://img.icons8.com/?size=100&id=uZWiLUyryScN&format=png&color=000000'>" : seller.contact_type.toLowerCase() === "discord" ? "<img width='15px' height='15px' src='https://img.icons8.com/?size=100&id=2mIgusGquJFz&format=png&color=000000'>" : seller.contact_type.toLowerCase() === "wechat" ? "<img width='20px' height='20px' src='https://img.icons8.com/?size=100&id=qXin8dFXNXBX&format=png&color=000000'/>" : "❌"}
            ${seller.contact_value}
            </td>
        `;
        table.appendChild(row);
    });
}
