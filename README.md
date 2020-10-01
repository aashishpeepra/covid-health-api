# covid-health-api project
This api returns data like real time corona cases and information. Along with health care centers, timeline of cases, cases district vise and much more.
<hr>

# Link
<a href="https://ironinfo.herokuapp.com/"> API is Hosted here </a>
Try routes like /info, /covidinfo?name=(hospital / covid / ircm / patient / heatmap) One at a time.

<h1> How To Use </h1>
<ul>
  <li> <a href="https://ironinfo.herokuapp.com/info">ironinfo.herokuapp.com/info</a> For Corona Cases</li>
  <li>
  For More Information /covidinfo?name=value. ( value can be following)
    <ul>
      <li> <a href="https://ironinfo.herokuapp.com/covidinfo?name=hospital">hospital</a> - For Hospitals Info</li>
      <li> <a href="https://ironinfo.herokuapp.com/covidinfo?name=covid">covid</a> - For cases Timeline</li>
      <li> <a href="https://ironinfo.herokuapp.com/covidinfo?name=ircm">ircm</a> - For IRCM info</li>
      <li> <a href="https://ironinfo.herokuapp.com/covidinfo?name=patient">patient</a> - For Patient info </li>
      <li> <a href="https://ironinfo.herokuapp.com/covidinfo?name=heatmap">heatmap</a> - For Geographical Data</li>
    </ul>
  </li>
</ul>

<h1> Technologies Used</h1>
<h2> APP </h2>
<ul>
  <li>Flask for Rest API</li>
  <li>Beautiful Soup for Scraping</li>
  <li> Pandas for data refining</li>
  <li> Added CORS into the Flask App</li>
</ul>
<h2> Hosting </h2>
<ul>
  <li> Heroku for hosting</li>
  <li> Gunicorn to serve Flask Application</li>
</ul>
<hr>


<h1> Throwback - Process</h1>
I had to create this API within one hour to integrate with my <a href="https://github.com/aashishpeepra/Corona-Relief-Admin-Panel" > Covid Relief Project</a>. So I had to cut and paste some static data. Other than that I have used the data from <a href="https://www.kaggle.com/">Kaggle</a> and scrapped corona cases details with Beautiful soup from <a href="https://www.worldometers.info/coronavirus/"> WorldOmeters</a>. The Scraping code was written by <a href="https://github.com/adarshSrivastava01"> <b> Adarsh Srivastava</b> </a>. I had to add CORS also in the api because some error with Vue.
<hr>
<h1> Forks are Welcome 🚀</h1>
