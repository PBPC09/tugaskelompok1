
    // Mengambil elemen input checkbox
    var checkbox = document.getElementById("flexSwitchCheckReverse");

    // Menambahkan event listener untuk mendengarkan perubahan status checkbox
    checkbox.addEventListener("change", function() {
        // Memeriksa apakah checkbox aktif atau tidak
        refreshForum();
    });

    let isBookClicked = false;

    $(document).ready(function() {
        $('.dropdown-menu').on('click', '.list-group-item', function() {
            var selectedItem = $(this).find('h5').text();
            var selectedBookId = $(this).data('id');        
            $('#book_id').val(selectedBookId);
            $('.dropdown-toggle').text(selectedItem);
            isBookClicked = true;
        });
    });


    const forumDataElement = document.getElementById('my-data');
    async function getForum() {
        const forumUrl = forumDataElement.getAttribute('data-forum-url');
        const popularForumUrl = forumDataElement.getAttribute('data-popular-forum-url');
        
        if(checkbox.checked == false){
            return fetch(forumUrl).then((res) => res.json());
        }
        else{
            return fetch(popularForumUrl).then((res) => res.json());
        }
    }
    async function getBook() {
        const bukuUrl = forumDataElement.getAttribute('data-buku');
        return fetch(bukuUrl).then((res) => res.json())
    }

    async function refreshForum() {
        document.getElementById("forum_container").innerHTML = "";
        const allForums = await getForum();

        let htmlString = `<table class="table table-row-spacing">
                            <tr style="height:50px;">
                                <th scope="col" style="width:400px;">Judul Topik</th>
                                <th scope="col" style="width:300px;">Buku</th>
                                <th scope="col" style="width:100px;">Penanya</th>
                                <th scope="col" style="width:100px;">Tanggal</th>
                                <th scope="col" style="width:100px;">Komentar</th>
                                <th scope="col" style="width:100px;"></th>
                            </tr>
                            <tbody class="table-group-divider">
        `;

        allForums.forEach((item) => {
            let database_url=forumDataElement.getAttribute('database-url');
            const rowUrl = database_url.replace('9999', item.pk);
            let deleteButton = '';
            if (item.fields.owned_by_current_user) {
                deleteButton = `<button class="btn btn-primary" style="font-size:12px;height: auto; text-align: center; background-color: #273faa;" onclick="event.stopPropagation(); deleteForum('${item.fields.user}',${item.pk}); return false; ">Delete</button>`;
            }
            console.log(item.fields.owned_by_current_user)
            htmlString += ` <tr class="mb-1 clickable-row " data-id="${item.pk}" data-url="${rowUrl}" style="height:50px;">
                                    <td class="overflow-control" style="width:400px; max-width: 385px;">${item.fields.title}</td>
                                    <td class="overflow-control" style="width:300px;max-width: 285px;">${item.fields.book}</td>
                                    <td class="overflow-control" style="width:100px;max-width: 100px;">${item.fields.user}</td>
                                    <td class="overflow-control" style="width:100px;max-width: 100px;">${item.fields.date}</td>
                                    <td class="overflow-control" style="width:100px;max-width: 100px;">${item.fields.comment_counts}</td>
                                    <td class="overflow-control" style="width:100px;max-width: 100px;"> 
                                        ${deleteButton}
                                    </td>
                            </tr>`
        });
        htmlString +=  `</tbody></table>`
        document.getElementById("forum_container").innerHTML = htmlString
        document.querySelectorAll('.clickable-row').forEach(row => {
        row.addEventListener('click', () => {
            const url = row.getAttribute('data-url');
            window.location.href = url;
            });
        });
    }

    function navigateToForum(url) {
        window.location.href = url;
    }

    refreshForum()

    async function showBooks(){
        document.getElementsByClassName("list-group")[0].innerHTML = "";
        const allBook = await getBook();
        let stringHTML="";
        allBook.forEach((item) => {
            stringHTML += `<a href="#" class="list-group-item list-group-item-action" data-id="${item.pk}">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">${item.fields.title}</h5>
                                <small class="text-body-secondary">${item.fields.rating}</small>
                        </div>
                        <p class="mb-1">${item.fields.author}</p>
                        <small class="text-body-secondary">${item.fields.publisher}</small>
                        </a>    `
        });
        document.getElementsByClassName("list-group")[0].innerHTML = stringHTML;
    }
    
    showBooks()

    function addForum() {
        let formData = new FormData(document.querySelector('#form'));
        let isEmptyFieldDetected = false;
        if(isBookClicked == false){
            alert("Pastikan semua terisi, silakan ulangi");
            return false;
        }
        for (let [key, value] of formData.entries()) {
            if (value.trim() === "") {
                isEmptyFieldDetected = true;
                break;
            }
        }

        if (isEmptyFieldDetected) {
            alert("Pastikan semua terisi, silakan ulangi");
            return false;
        }

        fetch(forumDataElement.getAttribute('create-question'), {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshForum)

        document.getElementById("form").reset()
        document.getElementById("dropdown-buku").innerText = "Pilih Buku"
        return false
    }

    document.getElementById("button_add").onclick = addForum

    function deleteForum(username,commentId) {
        const url = `/bookforum/delete_question/${username}/${commentId}`;
            fetch(url, {
                method: "GET",
            }).then(response => {
                if (response.status === 201) {
                    refreshForum();
                } else {
                    console.error("Failed to delete comment");
                    alert("Ini bukan pertanyaan dari akun Anda, Anda tidak bisa menghapusnya :)"); // Display an alert with an error message
                }
            })
            .catch(error => {
                console.error("Error deleting comment:", error);
                alert("Error deleting comment. Please try again later."); // Display an alert with an error message
            });
            return false
        }

