$(document).ready(function(){
    $("#cboCuidad").change(function(){

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
    });
});