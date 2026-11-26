// Screenshot driver: paste this whole block right before </body> in a COPY of the app's index.html,
// serve the folder locally (python3 -m http.server), then screenshot with Chrome headless:
//   chrome --headless=new --window-size=390,844 --device-scale-factor=2 --virtual-time-budget=12000 --screenshot=shots/preview.png "http://localhost:8931/index.html?shot=preview"
// Shots: landing, json, editor, images, print, preview

<script>
(function(){
  var shot=new URLSearchParams(location.search).get('shot');
  if(!shot||shot==='landing')return;
  function $(id){return document.getElementById(id)}
  function openStep(label){
    document.querySelectorAll('details.step').forEach(function(d){
      var t=d.querySelector('summary')?d.querySelector('summary').textContent:'';
      d.open = t.indexOf(label)>=0;
    });
  }
  window.addEventListener('load',function(){
    setTimeout(function(){
      var b=$('btn-landing-start'); if(b)b.click();
      setTimeout(function(){
        var ex=$('btn-example'); if(ex)ex.click();
        setTimeout(function(){
          if(shot==='editor')openStep('تحرير الأسئلة');
          else if(shot==='images')openStep('الصور');
          else if(shot==='print')openStep('القالب والإعدادات');
          else openStep('لصق');
          if(shot==='preview'){var tp=$('tab-preview'); if(tp)tp.click();}
          if(shot==='json'){var ta=document.getElementById('json-input'); var dd=ta?ta.closest('details'):null;
            document.querySelectorAll('details.step').forEach(function(d){d.open=(d===dd);});
            if(ta)ta.scrollIntoView({block:'center'});}
          else { var open=document.querySelector('details.step[open]');
            if(open&&shot!=='preview')open.scrollIntoView(); }
        },700);
      },700);
    },500);
  });
})();
</script>