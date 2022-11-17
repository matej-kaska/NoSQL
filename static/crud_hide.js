function edit(ide) {
    var nablok = ['pracoviste', 'telefon', 'email', 'pracovistetext', 'telefontext', 'emailtext', 'rem', 'upd'];
    for (i = 0; i < nablok.length; i++){
      const target = document.getElementById(ide + nablok[i]);

      if (target.style.display == "none") {
        target.style.display = "inline";
      } else {
        target.style.display = "none";
      }
    }
    
  };