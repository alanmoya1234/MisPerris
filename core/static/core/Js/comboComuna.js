

$(document).ready(function(){
    //realizar un evento ante algun cambio en el combo box de region
    $("#cboRegion").change(function(){

        var regionID=$("#cboRegion").val();

        if(regionID==""){
            $("#cboCuidad").prop("disabled",true);
            $("#cboCuidad").val("");

            var ciudadID=$("#cboCuidad").val();
        
                if(ciudadID==""){
                    $("#txtDireccion").prop("disabled",true);
                    $("#txtDireccion").val("");
                    return;
                }
                else{
                        $("#txtDireccion").prop("disabled",false);
                        return;
                }
                
            return;
        }
        $.get("/combo/"+regionID,function(respuesta){  //aca llame al combo (por e nombre) del urls.py que esta en core
            $("#cboCuidad").html(respuesta);
            $("#cboCuidad").prop("disabled",false);
        });

    });
});
