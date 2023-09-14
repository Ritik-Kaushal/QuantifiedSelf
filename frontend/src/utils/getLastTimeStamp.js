
function getLastTimestamp(days) {
    const now = new Date();
    var d = new Date(now.getTime() - days * 24 * 60 * 60 * 1000)
    var date = (d.toLocaleString(undefined, { day: '2-digit', month: '2-digit', year: 'numeric' })).split('/');
    var time = (d.toLocaleString('en-US', { hourCycle: 'h23', hour: '2-digit', minute: '2-digit', second: '2-digit' }));
    var timestamp = date[2] + '-' + date[1] + '-' + date[0] + ' ' + time;
    return timestamp;
}
export default getLastTimestamp;