html_1 = """
<!doctype html>
<html>
<head>
     <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="https://www.itxst.com/package/jquery-3.3.1/jquery.js"></script>
    <link href="https://www.itxst.com/package/bootstrap-4.3.1/css/bootstrap.css" rel="stylesheet" />
    <link href="https://www.itxst.com/package/bootstrap-table-1.15.3/bootstrap-table.css" rel="stylesheet" />
    <script src="https://www.itxst.com/package/bootstrap-table-1.15.3/bootstrap-table.js"></script>
    <title>"""

html_2="""
</title>
    <style>
        .table-demo {
            width: 80%;
            margin: 30px auto 0px auto;
        }
    </style>
</head>
<body>
<div id="toolbar" class="table-demo">
    <input type="text" id="start_time" placeholder="开始时间(单位为秒)">
    <input type="text" id="over_time" placeholder="结束时间(单位为秒)">
    <button onclick="update()" >时间段查找</button><br>
    <button onclick="s4()">恢复原始数据</button>
  </div>
    <div class="table-demo">
        <table id="table"></table>
    </div>
    <script>
"""

html_3 = """
 //bootstrap table初始化数据
        $('#table').bootstrapTable({
            columns: columns,
            data: data  ,
            search:'true',           // 确认打开全表搜索
            height:500,
        });
        function s4()
      {
      $('#start_time').val('');
        $('#over_time').val('');
       $('#table').bootstrapTable('filterBy', {},
       {
       'filterAlgorithm': function(row,filters)
        {
        
          return true;
        }
        });
      }
        """
html_4="""
         function update()
      {
          var start_time = $('#start_time').val();
          var over_time = $('#over_time').val();
          start_time = parseFloat(start_time);
          over_time=parseFloat(over_time);
      $('#table').bootstrapTable('filterBy', {Timepoint: [start_time,over_time]},
       {
       'filterAlgorithm': function(row,filters)
        {

           if(parseFloat(row.Timepoint)>=filters.Timepoint[0] && parseFloat(row.Timepoint)<=filters.Timepoint[1]) return true;
           // alert(JSON.stringify(filters));
          return false;
        }
        });
      }
      """
html_6 = """

         function update()
      {
          var start_time = $('#start_time').val();
          var over_time = $('#over_time').val();
          start_time = parseFloat(start_time);
          over_time=parseFloat(over_time);
      $('#table').bootstrapTable('filterBy', {Timestart: [start_time],Timeover:[over_time]},
       {
       'filterAlgorithm': function(row,filters)
        {var start_row = row.Timestart;
        var over_row = row.Timeover;
        start_row = parseFloat(start_row.substring(0,2))*3600+parseFloat(start_row.substring(3,5))*60+parseFloat(start_row.substring(6,8))+parseFloat(start_row.substring(9))/1000;
        over_row = parseFloat(over_row.substring(0,2))*3600+parseFloat(over_row.substring(3,5))*60+parseFloat(over_row.substring(6,8))+parseFloat(over_row.substring(9))/1000;
           if(start_row>=filters.Timestart[0] && over_row<=filters.Timeover[0]) return true;
           // alert(JSON.stringify(filters));
          return false;
        }
        });
      }
      """

html_5="""

    </script>
</body>
</html>
"""