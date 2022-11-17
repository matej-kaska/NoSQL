function edit(ide) {

    const more = document.getElementById(ide + 'rem');
    if (more.style.visibility == "hidden"){
      more.style.visibility = "visible";
    } else {
      more.style.visibility = "hidden";
    }
    
    const cs = document.getElementById(ide + 'upd');
    if (cs.style.visibility == "hidden"){
      cs.style.visibility = "visible";
    } else {
      cs.style.visibility = "hidden";
    }

    var nablok = ['pracoviste', 'telefon', 'email', , 'pracovistetext', 'telefontext', 'emailtext'];
    for (i = 0; i < nablok.length; i++){
      const target = document.getElementById(ide + nablok[i]);

      if (target.style.display == "none") {
        target.style.display = "block";
      } else {
        target.style.display = "none";
      }
    }
    
  };