    <script type="text/javascript">
    var pager = new Imtech.Pager();
    $(document).ready(function() {
        pager.paragraphsPerPage = 30; // set amount elements per page
        pager.pagingContainer = $('#players'); // set of main container
        pager.paragraphs = $('div.z', pager.pagingContainer); // set of required containers
        pager.showPage(1);
    });
    </script>


  <script> src="{{ url_for('static', filename='jquery.min.js') }}"</script>
  <script> src="{{ url_for('static', filename='imtech_pager.js') }}"</script>