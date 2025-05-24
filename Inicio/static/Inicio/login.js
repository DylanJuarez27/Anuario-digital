  const togglePassword = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('passwordInput');

  const toggleCodigoAcceso = document.getElementById('toggleCodigoAcceso')
  const codigoAccesoInput = document.getElementById('CodigoAccesoInput');
  
  const toggleIconPassword = document.getElementById('toggleIconPassword');
   
  const toggleIconCodigoAcceso = document.getElementById('toggleIconCodigoAcceso');

  togglePassword.addEventListener('click', function () {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    toggleIconPassword.classList.toggle('bi-eye-fill');
    toggleIconPassword.classList.toggle('bi-eye-slash-fill');
    
  });

  toggleCodigoAcceso.addEventListener('click', function () {
    const type = codigoAccesoInput.getAttribute('type') === 'password' ? 'text' : 'password';
    codigoAccesoInput.setAttribute('type', type);
    toggleIconCodigoAcceso.classList.toggle('bi-eye-fill');
    toggleIconCodigoAcceso.classList.toggle('bi-eye-slash-fill');
    
  });  