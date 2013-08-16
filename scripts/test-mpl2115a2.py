


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>bb_altimeter/scripts/mpl2115a2.py at master · vmayoral/bb_altimeter · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe118-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (2012-05-25, TCS patched 2012-05-27, GitHub v1.0.32) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="7luMv8TxG23SCLlpK/mUl58QisIyA1HFEtAJI5YDoUQ=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-2ecec547a18fa787eb84f55fb19e9ba1c121d4f9.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-37e86e426b1b017fee3061a69ac6d5eb2bb1a119.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-8c90145ced3264909647872c925b3f983056d3d1.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-bff8da3390ec6c158d36c0096c68911f0d98c19c.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="633fff549f918e1c427ec3fca8f29462">

        <link data-pjax-transient rel='permalink' href='/vmayoral/bb_altimeter/blob/11768dd5b804d7f2af11c91b2207ca48e573dfeb/scripts/mpl2115a2.py'>
  <meta property="og:title" content="bb_altimeter"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/vmayoral/bb_altimeter"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="bb_altimeter - ROS package for the BeagleBone that publishes the altimeter MPL3115A2 values to a Topic"/>

  <meta name="description" content="bb_altimeter - ROS package for the BeagleBone that publishes the altimeter MPL3115A2 values to a Topic" />

  <meta content="1375246" name="octolytics-dimension-user_id" /><meta content="vmayoral" name="octolytics-dimension-user_login" /><meta content="12016943" name="octolytics-dimension-repository_id" /><meta content="vmayoral/bb_altimeter" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="12016943" name="octolytics-dimension-repository_network_root_id" /><meta content="vmayoral/bb_altimeter" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/vmayoral/bb_altimeter/commits/master.atom" rel="alternate" title="Recent Commits to bb_altimeter:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production ">

    <div class="wrapper">
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/signup">Sign up</a>
      <a class="button" href="/login?return_to=%2Fvmayoral%2Fbb_altimeter%2Fblob%2Fmaster%2Fscripts%2Fmpl2115a2.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="vmayoral/bb_altimeter"
      data-branch="master"
      data-sha="c363b1e9c87669eb688886b8535dae304541bda8"
  >

    <input type="hidden" name="nwo" value="vmayoral/bb_altimeter" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
  <a href="/login?return_to=%2Fvmayoral%2Fbb_altimeter"
  class="minibutton with-count js-toggler-target star-button entice tooltipped upwards"
  title="You must be signed in to use this feature" rel="nofollow">
  <span class="octicon octicon-star"></span>Star
</a>
<a class="social-count js-social-count" href="/vmayoral/bb_altimeter/stargazers">
  1
</a>

  </li>

    <li>
      <a href="/login?return_to=%2Fvmayoral%2Fbb_altimeter"
        class="minibutton with-count js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/vmayoral/bb_altimeter/network" class="social-count">
        0
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/vmayoral" class="url fn" itemprop="url" rel="author"><span itemprop="title">vmayoral</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/vmayoral/bb_altimeter" class="js-current-repository js-repo-home-link">bb_altimeter</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/vmayoral/bb_altimeter" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /vmayoral/bb_altimeter">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/vmayoral/bb_altimeter/issues" aria-label="Issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /vmayoral/bb_altimeter/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/vmayoral/bb_altimeter/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /vmayoral/bb_altimeter/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/vmayoral/bb_altimeter/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /vmayoral/bb_altimeter/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/vmayoral/bb_altimeter/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /vmayoral/bb_altimeter/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/vmayoral/bb_altimeter/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /vmayoral/bb_altimeter/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    </ul>

  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/vmayoral/bb_altimeter.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/vmayoral/bb_altimeter.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/vmayoral/bb_altimeter" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/vmayoral/bb_altimeter" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>



                <a href="/vmayoral/bb_altimeter/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:bfb04d2de18a8c905514567b08c3836f -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:bfb04d2de18a8c905514567b08c3836f -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/vmayoral/bb_altimeter/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/vmayoral/bb_altimeter/blob/master/scripts/mpl2115a2.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/vmayoral/bb_altimeter" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">bb_altimeter</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/vmayoral/bb_altimeter/tree/master/scripts" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">scripts</span></a></span><span class="separator"> / </span><strong class="final-path">mpl2115a2.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="scripts/mpl2115a2.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://2.gravatar.com/avatar/1d2974926bbbd4c31f04f7d2645e44b7?s=140&amp;d=https%3A%2F%2Fidenticons.github.com%2F860ab8a7639ebba17142e51d6dee4c4a.png" width="24" />
    <span class="author"><a href="/vmayoral" rel="author">vmayoral</a></span>
    <time class="js-relative-date" datetime="2013-08-16T11:43:57-07:00" title="2013-08-16 11:43:57">August 16, 2013</time>
    <div class="commit-title">
        <a href="/vmayoral/bb_altimeter/commit/11768dd5b804d7f2af11c91b2207ca48e573dfeb" class="message" data-pjax="true" title="the driver gets the values from the sensor however the altimeter is some...

...how 100 meters wrong">the driver gets the values from the sensor however the altimeter is s…</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://2.gravatar.com/avatar/1d2974926bbbd4c31f04f7d2645e44b7?s=140&amp;d=https%3A%2F%2Fidenticons.github.com%2F860ab8a7639ebba17142e51d6dee4c4a.png" width="24" />
          <a href="/vmayoral">vmayoral</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>79 lines (70 sloc)</span>
        <span>2.343 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton js-entice" href=""
                 data-entice="You must be signed in to make or propose changes">Edit</a>
          <a href="/vmayoral/bb_altimeter/raw/master/scripts/mpl2115a2.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/vmayoral/bb_altimeter/blame/master/scripts/mpl2115a2.py" class="button minibutton ">Blame</a>
          <a href="/vmayoral/bb_altimeter/commits/master/scripts/mpl2115a2.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon js-entice" href=""
               data-entice="You must be signed in and on a branch to make or propose changes">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC2'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">i2ctools_python</span> <span class="kn">import</span> <span class="n">I2C</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC5'><span class="c">#MPL3115A register address</span></div><div class='line' id='LC6'><span class="n">MPL3115_STATUS</span>              <span class="o">=</span><span class="s">&quot;0x00&quot;</span></div><div class='line' id='LC7'><span class="n">MPL3115_PRESSURE_DATA</span>       <span class="o">=</span><span class="s">&quot;0x01&quot;</span></div><div class='line' id='LC8'><span class="n">MPL3115_DR_STATUS</span>           <span class="o">=</span><span class="s">&quot;0x06&quot;</span></div><div class='line' id='LC9'><span class="n">MPL3115_DELTA_DATA</span>          <span class="o">=</span><span class="s">&quot;0x07&quot;</span></div><div class='line' id='LC10'><span class="n">MPL3115_WHO_AM_I</span>            <span class="o">=</span><span class="s">&quot;0x0c&quot;</span></div><div class='line' id='LC11'><span class="n">MPL3115_FIFO_STATUS</span>         <span class="o">=</span><span class="s">&quot;0x0d&quot;</span></div><div class='line' id='LC12'><span class="n">MPL3115_FIFO_DATA</span>           <span class="o">=</span><span class="s">&quot;0x0e&quot;</span></div><div class='line' id='LC13'><span class="n">MPL3115_FIFO_SETUP</span>          <span class="o">=</span><span class="s">&quot;0x0e&quot;</span></div><div class='line' id='LC14'><span class="n">MPL3115_TIME_DELAY</span>          <span class="o">=</span><span class="s">&quot;0x10&quot;</span></div><div class='line' id='LC15'><span class="n">MPL3115_SYS_MODE</span>            <span class="o">=</span><span class="s">&quot;0x11&quot;</span></div><div class='line' id='LC16'><span class="n">MPL3115_INT_SORCE</span>           <span class="o">=</span><span class="s">&quot;0x12&quot;</span></div><div class='line' id='LC17'><span class="n">MPL3115_PT_DATA_CFG</span>         <span class="o">=</span><span class="s">&quot;0x13&quot;</span></div><div class='line' id='LC18'><span class="n">MPL3115_BAR_IN_MSB</span>          <span class="o">=</span><span class="s">&quot;0x14&quot;</span></div><div class='line' id='LC19'><span class="n">MPL3115_P_ARLARM_MSB</span>        <span class="o">=</span><span class="s">&quot;0x16&quot;</span></div><div class='line' id='LC20'><span class="n">MPL3115_T_ARLARM</span>            <span class="o">=</span><span class="s">&quot;0x18&quot;</span></div><div class='line' id='LC21'><span class="n">MPL3115_P_ARLARM_WND_MSB</span>    <span class="o">=</span><span class="s">&quot;0x19&quot;</span></div><div class='line' id='LC22'><span class="n">MPL3115_T_ARLARM_WND</span>        <span class="o">=</span><span class="s">&quot;0x1b&quot;</span></div><div class='line' id='LC23'><span class="n">MPL3115_P_MIN_DATA</span>          <span class="o">=</span><span class="s">&quot;0x1c&quot;</span></div><div class='line' id='LC24'><span class="n">MPL3115_T_MIN_DATA</span>          <span class="o">=</span><span class="s">&quot;0x1f&quot;</span></div><div class='line' id='LC25'><span class="n">MPL3115_P_MAX_DATA</span>          <span class="o">=</span><span class="s">&quot;0x21&quot;</span></div><div class='line' id='LC26'><span class="n">MPL3115_T_MAX_DATA</span>          <span class="o">=</span><span class="s">&quot;0x24&quot;</span></div><div class='line' id='LC27'><span class="n">MPL3115_CTRL_REG1</span>           <span class="o">=</span><span class="s">&quot;0x26&quot;</span></div><div class='line' id='LC28'><span class="n">MPL3115_CTRL_REG2</span>           <span class="o">=</span><span class="s">&quot;0x27&quot;</span></div><div class='line' id='LC29'><span class="n">MPL3115_CTRL_REG3</span>           <span class="o">=</span><span class="s">&quot;0x28&quot;</span></div><div class='line' id='LC30'><span class="n">MPL3115_CTRL_REG4</span>           <span class="o">=</span><span class="s">&quot;0x29&quot;</span></div><div class='line' id='LC31'><span class="n">MPL3115_CTRL_REG5</span>           <span class="o">=</span><span class="s">&quot;0x2a&quot;</span></div><div class='line' id='LC32'><span class="n">MPL3115_OFFSET_P</span>            <span class="o">=</span><span class="s">&quot;0x2b&quot;</span></div><div class='line' id='LC33'><span class="n">MPL3115_OFFSET_T</span>            <span class="o">=</span><span class="s">&quot;0x2c&quot;</span></div><div class='line' id='LC34'><span class="n">MPL3115_OFFSET_H</span>            <span class="o">=</span><span class="s">&quot;0x2d&quot;</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="c">######################################</span></div><div class='line' id='LC37'><span class="c"># Check if i2c-tools are properly installed</span></div><div class='line' id='LC38'><span class="n">device</span> <span class="o">=</span> <span class="n">I2C</span><span class="p">()</span></div><div class='line' id='LC39'><span class="n">device</span><span class="o">.</span><span class="n">check_i2ctools</span><span class="p">()</span></div><div class='line' id='LC40'><span class="c">######################################</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'><span class="c"># Set to Altimeter with an OSR = 128 </span></div><div class='line' id='LC43'><span class="n">device</span><span class="o">.</span><span class="n">writeI2C</span><span class="p">(</span><span class="n">MPL3115_CTRL_REG1</span><span class="p">,</span> <span class="s">&quot;0xB8&quot;</span><span class="p">)</span></div><div class='line' id='LC44'><span class="c"># Enable Data Flags in PT_DATA_CFG</span></div><div class='line' id='LC45'><span class="n">device</span><span class="o">.</span><span class="n">writeI2C</span><span class="p">(</span><span class="n">MPL3115_PT_DATA_CFG</span><span class="p">,</span> <span class="s">&quot;0x07&quot;</span><span class="p">)</span></div><div class='line' id='LC46'><span class="c"># Set Active (polling)</span></div><div class='line' id='LC47'><span class="n">device</span><span class="o">.</span><span class="n">writeI2C</span><span class="p">(</span><span class="n">MPL3115_CTRL_REG1</span><span class="p">,</span> <span class="s">&quot;0xB9&quot;</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read STATUS Register</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">STA</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">readI2C</span><span class="p">(</span><span class="n">MPL3115_STATUS</span><span class="p">)</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># check if pressure or temperature are ready (both) [STATUS, 0x00 register]</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">STA</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;error with the sensor&quot;</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">STA</span><span class="p">,</span><span class="mi">16</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0x04</span><span class="p">)</span> <span class="o">==</span> <span class="mi">4</span><span class="p">:</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># OUT_P</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OUT_P_MSB</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">readI2C</span><span class="p">(</span><span class="s">&quot;0x01&quot;</span><span class="p">)</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OUT_P_CSB</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">readI2C</span><span class="p">(</span><span class="s">&quot;0x02&quot;</span><span class="p">)</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OUT_P_LSB</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">readI2C</span><span class="p">(</span><span class="s">&quot;0x04&quot;</span><span class="p">)</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## OUT_T</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#OUT_T_MSB = readI2C(0x04)</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#OUT_T_LSB = readI2C(0x05)</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">OUT_P_MSB</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">OUT_P_CSB</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">OUT_P_LSB</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#treat the bits to get the altitude</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">signedvalue</span> <span class="o">=</span> <span class="n">OUT_P_MSB</span><span class="o">+</span><span class="n">OUT_P_CSB</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fraction</span> <span class="o">=</span> <span class="n">OUT_P_LSB</span><span class="p">[:</span><span class="mi">3</span><span class="p">]</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="nb">int</span><span class="p">(</span><span class="n">signedvalue</span><span class="p">,</span><span class="mi">16</span><span class="p">)</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="nb">int</span><span class="p">(</span><span class="n">fraction</span><span class="p">,</span><span class="mi">16</span><span class="p">)</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#print &quot;data not ready&quot;</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.04924s from github-fe118-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/vmayoral/bb_altimeter/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

