function addResult(title,result){
    fetch("/saveResult",{
        method:'POST',
        body:JSON.stringify({title:title,result:result})
    }).then((_res)=>{
        window.location.href='/history';
    })
}