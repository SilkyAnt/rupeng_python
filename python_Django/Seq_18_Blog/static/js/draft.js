document.getElementById("deleteBtn").onclick=function (ev) {
    if(confirm("确实要删除该条博客么?")){
        return true
    }else{
        return false
    }
}