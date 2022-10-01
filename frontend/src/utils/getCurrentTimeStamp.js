function getCurrentTimestamp(){
    var date=(new Date().toLocaleString(undefined,{day:'2-digit', month:'2-digit',year:'numeric'})).split('/');
    var time=(new Date().toLocaleString('en-US',{hour12: false,hour:'2-digit',minute:'2-digit',second:'2-digit'}));
    var timestamp = date[2]+'-'+date[0]+'-'+date[1]+' '+time;
    return timestamp;

}
export default getCurrentTimestamp;