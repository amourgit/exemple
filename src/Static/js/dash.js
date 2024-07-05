// script.js
// Affichage du dashboard au chargement de la page


document.addEventListener('DOMContentLoaded', function() {
    const notificationElement = document.getElementById('commande-notification');
    const Total_bon_commande = document.getElementById('bon-commande');
    const historiqueMouvements = document.getElementById('historique-mouvements');
    const totalFiltre = document.getElementById('total-filtre');
    const navLinks = document.querySelectorAll('.nav-link');
    const tabContents = document.querySelectorAll('.tab-content');
    const tab_history = document.getElementById('historique-mouvements');
    

    //   Gestion de l'affichage et de la modal pour les entrée et sortie
    const modal = document.getElementById('modalEntreeSortie');
    const modalTitle = document.getElementById('modalTitle');
    const type_mouv = document.getElementById('type_mouvement');
    const entreeSortieForm = document.getElementById('entreeSortieForm');

    totalFiltre.textContent = `Total: ${historiqueMouvements.children.length}`;
    notificationElement.textContent = `${Total_bon_commande.children.length}`;
    console.log(Number(notificationElement.textContent))
    if (Number(notificationElement.textContent)==0) {
        notificationElement.classList.add('hidden');
    } else {
        notificationElement.classList.remove('hidden');
    }
  

    const big_entre = document.getElementById('liste-entrees');
    const big_sortie = document.getElementById('liste-sorties');
    const big_stock = document.getElementById('article-list');
    const totalEntrees = document.getElementById('total-entrees');
    const totalSorties = document.getElementById('total-sorties');
    const totalStock = document.getElementById('total-stock');
    let nb_entree = big_entre.children.length;
    let nb_sortie = big_sortie.children.length;
    let nb_stock = big_stock.children.length;
    console.log(nb_sortie);
    let cal_entree = 0;
    let cal_sortie = 0;
    let cal_stock = 0;
    let i = 0;
    let j = 0;
    let k = 0;
    while (i < nb_sortie){
        var item = big_sortie.children[i];
        cal_sortie = cal_sortie + Number(item.children[1].textContent);
        i++;
    };
    
    while (j < nb_entree){
        var item = big_entre.children[j];
        cal_entree = cal_entree + Number(item.children[1].textContent);
        j++;
    };

    while (k < nb_stock){
        var item = big_stock.children[k];
        cal_stock = cal_stock + Number(item.children[2].textContent);
        k++;
    };

    totalSorties.textContent = cal_sortie;
    totalEntrees.textContent = cal_entree;
    totalStock.textContent = cal_stock;




//  Systéme pour passer d'un onglets à un autres
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const tab = link.getAttribute('data-tab');

            navLinks.forEach(nav => nav.classList.remove('active'));
            link.classList.add('active');

            tabContents.forEach(content => {
                content.classList.toggle('active', content.id === tab);
            });
        });
    });

    /*const content_hist = tab_history.innerHTML;
    document.getElementById('filter-btn').addEventListener('click', function() {
        tab_history.innerHTML = content_hist;
        var critere = document.getElementById('filter-type').value;
        if (critere == '') {
            tab_history.innerHTML = content_hist;
        } else {
            let i = 0;
            var tbody = document.createElement('tbody');
            var newRow = document.createElement('tr');
            while (i < tab_history.children.length) {
                var critere = document.getElementById('filter-type').value;
                var item = tab_history.children[i];
                if (critere == item.children[0].textContent){
                    console.log(`Les  ${item.children[0].textContent}`);
                    newRow.innerHTML = `${(item.innerHTML)}`;
                    tbody.appendChild(newRow.innerHTML);
                };
                i++;
            };
            tab_history.innerHTML = tbody.innerHTML;
        };
    });*/

    document.getElementById('filter-btn').addEventListener('click', function() {
        //const filterDate = document.getElementById('filter-date').value;
        const filterType = document.getElementById('filter-type').value;
        const historiqueMouvements = document.getElementById('historique-mouvements');
        historiqueMouvements.innerHTML = '';

        const filterRows = (rows, type) => {
            rows.forEach(row => {
                const date = row.children[4].textContent;
                const typeMouvement = type === 'entree' ? 'Entrée' : 'Sortie';
                if (filterType === '' || filterType === type) {
                    const newRow = document.createElement('tr');
                    newRow.innerHTML = `
                        <td class="py-2 px-4">${typeMouvement}</td>
                        <td class="py-2 px-4">${row.children[0].textContent}</td>
                        <td class="py-2 px-4">${row.children[1].textContent}</td>
                        <td class="py-2 px-4">${row.children[2].textContent}</td>
                        <td class="py-2 px-4">${row.children[3].textContent}</td>
                        <td class="py-2 px-4">${date}</td>
                    `;
                    historiqueMouvements.appendChild(newRow);
                }
            });
        };

        filterRows(document.querySelectorAll('#liste-entrees tr'), 'entree');
        filterRows(document.querySelectorAll('#liste-sorties tr'), 'sortie');

        const totalFiltre = document.getElementById('total-filtre');
        totalFiltre.textContent = `Total: ${historiqueMouvements.children.length}`;
    });



//  Gestion de la modal pour l'affichage de la modal au click des boutton ajouter une entrée et une sortie
    let currentType = '';
    
    document.getElementById('ajouter-entree-btn').addEventListener('click', function() {
        currentType = 'entree';
        type_mouv.value = 'Entree';
        modalTitle.textContent = 'Ajouter une Entrée';
        modal.classList.add('active');
    });


    document.getElementById('ajouter-sortie-btn').addEventListener('click', function() {
        currentType = 'sortie';
        type_mouv.value = 'Sortie';
        modalTitle.textContent = 'Ajouter une Sortie';
        modal.classList.add('active');
    });

    document.getElementById('cancelBtn').addEventListener('click', function() {
        modal.classList.remove('active');
        entreeSortieForm.reset();
    });


    document.getElementById('download-pdf-btn').addEventListener('click', function() {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        const articleList = [];
        const bon_commande = document.getElementById('bon-commande');

    
        // Informations de l'entreprise
        const nomEntreprise = 'D-ONE E-TECH';
        const adresseEntreprise = 'PK8 DANS LES GALERIES MINOUCHE';
        const telEntreprise = '066515677/ 077297795';
        const emailEntreprise = 'd.oneetech@gmail.com ';
        const lien_mere = document.getElementById('lien_mere').textContent;

        const logoUrl = lien_mere+'/Static/images/image.png'; 
    
        // Ajout du logo
        const img = new Image();
        img.src = logoUrl;
        img.onload = function() {
            // logo (coordonnées x, y, largeur, hauteur)
            doc.addImage(img, 'png', 10, 10, 30, 30);
        };
            // informations de l'entreprise
            doc.setFontSize(12);
            doc.text(nomEntreprise, 50, 15);
            doc.text(adresseEntreprise, 50, 22);
            doc.text(`Tel: ${telEntreprise}`, 50, 29);
            doc.text(`Email: ${emailEntreprise}`, 50, 36);
    
            // Titre du PDF
            doc.setFontSize(18);
            doc.setFont('helvetica', 'bold')
            doc.text('Bon de Commande', doc.internal.pageSize.width / 2, 50, { align: 'center' });
    
            // Colonnes du tableau
            const headers = [['Désignation', 'Quantité']];
            
            var val = {};
            let i = 0;
            while (i < (bon_commande.children.length)){
                var item = bon_commande.children[i];
                val = { libelle: item.children[1].textContent, quantite: item.children[2].textContent };
                articleList.push(val);
                i++;
            };

    
            // Contenu du tableau
            const data = articleList.map(article => [article.libelle, article.quantite]);

            // Ajout du tableau au PDF
            doc.autoTable({
                head: headers,
                body: data,
                startY: 60,
                theme: 'grid',
                styles: {
                    fontSize: 12,
                    halign: 'center',
                }
            });
    
            // Ajout du bas de page
            doc.setFontSize(10);
            doc.text('Merci de vérifier la disponibilité des articles avant de commander.', 20, doc.internal.pageSize.height - 30);
            doc.text('Contactez-nous pour plus d\'informations.', 20, doc.internal.pageSize.height - 20);
    
            // Téléchargement du PDF
            doc.save('Bon de Commande.pdf');
        });
    });
    



