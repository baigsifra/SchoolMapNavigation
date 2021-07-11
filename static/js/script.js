let intro = document.querySelector('.intro');
let logoSpan = document.querySelectorAll('.logo');

window.addEventListener('DOMContentLoaded', ()=>{
  setTimeout(()=>{
    logoSpan.forEach((span, idx)=>{
      setTimeout(()=>{
        span.classList.add('active');
      }, (idx + 1) * 400)
    });
    setTimeout(()=>{
      logoSpan.forEach((span, idx)=>{
        setTimeout(()=>{
          span.classList.remove('active');
          span.classList.add('fade');
        }, (idx + 1 * 50))
      })
    }, 2000);
    setTimeout(()=>{
      intro.style.top = '-100vh';
    }, 2300)
  })
} )

let submit = document.getElementById('upload-file');

submit.onchange = function() {
  let fileName = '';
  fileName = submit.value;
  document.getElementById('file-selected').innerHTML = fileName; 
};