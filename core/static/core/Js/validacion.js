$(document).ready(function(){
    $("#formularioSocio").validate({
        rules:
        {
            txtRun:{
                required:true,
                minlength:9
            },
            txtNombre:{
                required:true
            },
            txtApPat:{
                required:true
            },
            txtApMat:{
                required:true
            },
            cboGenero:{
                required:true
            },            
            txtMail:{
                required:true,
                email:true
            },
            txtNacimiento:{
                required:true
            },
            txtfono:{

            },
            cboRegion:{
                required:true
            },
            cboCuidad:{
                required:true
            },
            cboTipoVivienda:{
                required:true
            },
            txtDireccion:{
                required:true
            },
            cboUser:{
                required:true
            }
        },
        messages:
        {
            txtNombre:{
                required:"Campo obligatorio (*)"
            },
            txtApPat:{
                required:"Campo obligatorio (*)"
            },
            txtApMat:{
                required:"Campo obligatorio (*)"
            },
            cboGenero:{
                required:"Campo obligatorio (*)"
            },  
            txtRun:{
                required:"Campo obligatorio (*)",
                minlength:"Minimo 9 digitos"

            },
            txtMail:{
                required:"Campo obligatorio (*)",
                email:"Ingrese un mail valido"
            },
            txtNacimiento:{
                required:"Campo obligatorio (*)"
            },
            txtfono:{

            },
            cboRegion:{
                required:"Campo obligatorio (*)"
            },
            cboCuidad:{
                required:"Campo obligatorio (*)"
            },
            cboTipoVivienda:{
                required:"Campo obligatorio (*)"
            },
            txtDireccion:{
                required:"Campo obligatorio (*)"
            },
            cboUser:{
                required:"Campo obligatorio (*)"
            }
        }
    });
});

