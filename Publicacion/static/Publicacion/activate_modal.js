document.addEventListener('DOMContentLoaded', function () {
  const hash = window.location.hash;

  if (hash && hash.startsWith("#modal")) {
    const regex = /#modal(\d+)(-comentarios)?/;
    const match = hash.match(regex);

    if (match) {
      const publicacionId = match[1];
      const mostrarComentarios = !!match[2];

      const modalEl = document.querySelector(`#modal${publicacionId}`);
      if (modalEl) {
        const modal = new bootstrap.Modal(modalEl);

        modalEl.addEventListener('shown.bs.modal', function () {
          if (mostrarComentarios) {
            const comentariosTabTrigger = document.querySelector(`#comentarios-tab${publicacionId}`);
            if (comentariosTabTrigger) {
              new bootstrap.Tab(comentariosTabTrigger).show();
            }
          }
        });

        modal.show();
      }
    }
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const hash = window.location.hash;
  if (!hash) return;


  const [tabId, modalId] = hash.replace('#', '').split('-'); 


  if (tabId && document.getElementById(`${tabId}-tab`)) {
    const tabTrigger = document.getElementById(`${tabId}-tab`);
    new bootstrap.Tab(tabTrigger).show();
  }

 
  if (modalId) {
    setTimeout(() => {
      const modalEl = document.getElementById(modalId);
      if (modalEl) {
        const modal = new bootstrap.Modal(modalEl);

     
        modalEl.addEventListener('hidden.bs.modal', function () {
          document.body.classList.remove('modal-open');
          const backdrops = document.querySelectorAll('.modal-backdrop');
          backdrops.forEach(b => b.remove());
        });

        modal.show();
      }
    }, 500); 
  }
});


document.addEventListener("DOMContentLoaded", function () {
  $('#agregarPremio').on('shown.bs.modal', function () {
    $('.select2').select2({
      dropdownParent: $('#agregarPremio') 
    });
  });
});

