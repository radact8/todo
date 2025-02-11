document.querySelector('form').addEventListener('submit',function(event){
    var formName = event.target.name;
    console.log(formName);
})