const btnDelete = document.querySelectorAll('.btn-delete');

if (btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{
            var ask = confirm('Are you sure you want to delete it?');
            if(!ask){
                e.preventDefault();
          }
        });
    });
}