var Tabulator = require('tabulator-tables');

var table = new Tabulator("example", {
    columns:[
        {title:"Name", field:"name", sorter:"string", width:200, editor:true},
        {title:"Age", field:"age", sorter:"number", align:"right", formatter:"progress"},
        {title:"Gender", field:"gender", sorter:"string", cellClick:function(e, cell){console.log("cell click")},},
        {title:"Height", field:"height", formatter:"star", align:"center", width:100},
        {title:"Favourite Color", field:"col", sorter:"string"},
        {title:"Date Of Birth", field:"dob", sorter:"date", align:"center"},
        {title:"Cheese Preference", field:"cheese", sorter:"boolean", align:"center", formatter:"tickCross"},
    ],
});