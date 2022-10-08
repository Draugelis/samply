# flake8: noqa

test_search_page_success = """
<body>
<div class="ad-slot">
<div class="top-ad ">
<div id="cmn-leaderboard" class="fw_whosampled">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['top', 'cmn-leaderboard']]);
        </script>
<div id="cmn_wrap">
<header id="header">
<div class="nav" id="js-nav">
<div class="nav-wrap">
<div class="logo-wrapper">
<a href="/" class="logo" aria-label="WhoSampled logo"></a>
</div>
<div class="nav-top">
<div class="socialMedia nav-top-social">
<a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
</div>
<nav class="userLinks nav-top-user">
<div class="nav-inner">
<div class="signin-wrapper mobile">
<a href="/user/login/" rel="nofollow" class="avatar">
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M18 22.082v-1.649c2.203-1.241 4-4.337 4-7.432 0-4.971 0-9-6-9s-6 4.029-6 9c0 3.096 1.797 6.191 4 7.432v1.649C7.216 22.637 2 25.97 2 30h28c0-4.03-5.216-7.364-12-7.918z"></path></svg>
</a>
</div>
<div class="signin-wrapper desktop">
<a href="/user/registration/" rel="nofollow" class="btn signup">Sign up</a> <a href="/user/login/" rel="nofollow" class="btn signin">Sign in</a>
</div>
</div>
</nav>
</div>
<div class="nav-main">
<nav class="nav-links">
<ul>
<li><a href="/news/">News</a></li>
<li><a href="/browse/">Browse</a></li>
<li><a href="/charts/">Charts</a></li>
<li class="nav-submit"><a href="/submit/" class="loginButton">Submit</a></li>
<li><a href="/six-degrees/">6º Game</a></li>
</ul>
</nav>
<form action="/search/" method="get" id="search-bar" class="searchForm nav-search">
<input type="text" id="searchInput" class="searchInput text" name="q" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="none" placeholder="Track, Artist, Movie, TV show" value="Nas ny state of mind" maxlength="80" aria-label="Type any track, artist, movie or TV show">
<span class="loading" style="display:none"></span>
<span class="submit-wrapper"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M31.008 27.231l-7.58-6.447c-.784-.705-1.622-1.029-2.299-.998a11.954 11.954 0 0 0 2.87-7.787c0-6.627-5.373-12-12-12s-12 5.373-12 12 5.373 12 12 12c2.972 0 5.691-1.081 7.787-2.87-.031.677.293 1.515.998 2.299l6.447 7.58c1.104 1.226 2.907 1.33 4.007.23s.997-2.903-.23-4.007zM12 20a8 8 0 1 1 0-16 8 8 0 0 1 0 16z"></path></svg><input type="submit" class="submit" value="" aria-label="Search"></span>
</form>
</div>
</div>
</div>
</header>
<main role="main" id="container" class="main-container">
<div id="searchDropdown" class="dropdown search-dropdown" style="display:none">
<div id="searchArtists">
<span class="searchType">Artists</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTracks">
<span class="searchType">Tracks</span>
<ul class="searchList">
</ul>
</div>
<div id="searchMovies">
<span class="searchType">Movies</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTVShows">
<span class="searchType">TV Shows</span>
<ul class="searchList">
</ul>
</div>
</div>
<div class="spSlot">
<a href="/mobile-app/get/" target="_blank" rel="noopener">
<picture>
<source type="image/avif" srcset="/static/images/banners/app-banner-desktop-1100x131.avif 1x, /static/images/banners/app-banner-desktop-2200x261.avif 2x">
<source type="image/webp" srcset="/static/images/banners/app-banner-desktop-1100x131.webp 1x, /static/images/banners/app-banner-desktop-2200x261.webp 2x">
<img src="/static/images/banners/app-banner-desktop-1100x131.jpg" srcset="/static/images/banners/app-banner-desktop-1100x131.jpg 1x, /static/images/banners/app-banner-desktop-2200x261.jpg 2x" width="1100" height="131">
</picture>
</a>
</div>
<div id="content">
<div class="divided-layout search-results">
<div class="leftContent">
<h1 class="headTitle">Search Results for “Nas ny state of mind”</h1>
<div class="searchTypes">
Search:
<strong>All Music</strong> |
<a href="/search/tracks/?q=Nas ny state of mind">Tracks</a> |
<a href="/search/connections/?q=Nas ny state of mind">Connections</a>
</div>
<div class="sectionHeader">
<h2>Top hit</h2>
</div>
<div class="topHit">
<div class="image"><a href="/Nas/N.Y.-State-of-Mind/"><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" alt="Nas's N.Y. State of Mind" width="100" height="100"></a></div>
<div class="title">
<a class="trackTitle" href="/Nas/N.Y.-State-of-Mind/">N.Y. State of Mind</a>
<span class="trackArtist">by <a href="/Nas/">Nas</a></span>
</div>
</div>
<div class="sectionHeader">
<h2>Tracks</h2>
</div>
<ul class="list bordered-list">
<li class="listEntry trackEntry">
<a href="/Nas/N.Y.-State-of-Mind,-Pt.-II/" title="Nas's N.Y. State of Mind, Pt. II"><img loading="lazy" src="/static/track_images_100/mr16478_20101114_231410204378.jpg" srcset="/static/track_images_100/mr16478_20101114_231410204378.jpg 1x, /static/track_images_200/lr16478_20101114_231410204378.jpg 2x" width="80" height="80"></a>
<span class="trackDetails">
<a class="trackName" href="/Nas/N.Y.-State-of-Mind,-Pt.-II/" title="Nas's N.Y. State of Mind, Pt. II">N.Y. State of Mind, Pt. II</a>
<span class="trackArtist">by <a href="/Nas/">Nas</a> (1999)</span>
</span>
</li>
</ul>
<div class="sectionHeader">
<h2>Connections</h2>
<a href="/search/connections/?q=Nas ny state of mind" class="moreButton">see more connections</a>
</div>
<ul class="list bordered-list">
<li class="listEntry sampleCompactEntry">
<a href="/sample/896/Nas-N.Y.-State-of-Mind-Joe-Chambers-Mind-Rain/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/896/Nas-N.Y.-State-of-Mind-Joe-Chambers-Mind-Rain/">Nas's N.Y. State of Mind <span class="sampleType">sample of</span> Joe Chambers's Mind Rain</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/10075/Nas-N.Y.-State-of-Mind-Donald-Byrd-Flight-Time/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/10075/Nas-N.Y.-State-of-Mind-Donald-Byrd-Flight-Time/">Nas's N.Y. State of Mind <span class="sampleType">sample of</span> Donald Byrd's Flight Time</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/109933/Nas-N.Y.-State-of-Mind-Kool-%26-the-Gang-N.T./" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/109933/Nas-N.Y.-State-of-Mind-Kool-%26-the-Gang-N.T./">Nas's N.Y. State of Mind <span class="sampleType">sample of</span> Kool &amp; the Gang's N.T.</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/12391/Nas-N.Y.-State-of-Mind-Eric-B.-%26-Rakim-Mahogany/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/12391/Nas-N.Y.-State-of-Mind-Eric-B.-%26-Rakim-Mahogany/">Nas's N.Y. State of Mind <span class="sampleType">sample of</span> Eric B. &amp; Rakim's Mahogany</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/70550/Nas-N.Y.-State-of-Mind,-Pt.-II-Donald-Byrd-Flight-Time/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr16478_20101114_231410204378.jpg" srcset="/static/track_images_100/mr16478_20101114_231410204378.jpg 1x, /static/track_images_200/lr16478_20101114_231410204378.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/70550/Nas-N.Y.-State-of-Mind,-Pt.-II-Donald-Byrd-Flight-Time/">Nas's N.Y. State of Mind, Pt. II <span class="sampleType">sample of</span> Donald Byrd's Flight Time</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/22883/Nas-N.Y.-State-of-Mind-Main-Source-Nas-Joe-Fatal-Akinyele-Live-at-the-Barbeque/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/22883/Nas-N.Y.-State-of-Mind-Main-Source-Nas-Joe-Fatal-Akinyele-Live-at-the-Barbeque/">Nas's N.Y. State of Mind <span class="sampleType">sample of</span> Main Source feat. Nas, Joe Fatal and Akinyele's Live at the Barbeque</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/22232/Nas-The-Message-Nas-N.Y.-State-of-Mind/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr3_2008121_154123589498.jpg" srcset="/static/track_images_100/mr3_2008121_154123589498.jpg 1x, /static/track_images_200/lr3_2008121_154123589498.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/22232/Nas-The-Message-Nas-N.Y.-State-of-Mind/">Nas's The Message <span class="sampleType">sample of</span> Nas's N.Y. State of Mind</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/47105/Alicia-Keys-Nas-Rakim-Streets-of-New-York-Nas-N.Y.-State-of-Mind/" title="Alicia Keys and Nas feat. Rakim's "><img loading="lazy" src="/static/track_images_100/mr2929_201075_92223803556.jpg" srcset="/static/track_images_100/mr2929_201075_92223803556.jpg 1x, /static/track_images_200/lr2929_201075_92223803556.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/47105/Alicia-Keys-Nas-Rakim-Streets-of-New-York-Nas-N.Y.-State-of-Mind/">Alicia Keys and Nas feat. Rakim's Streets of New York <span class="sampleType">sample of</span> Nas's N.Y. State of Mind</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/68582/Nas-N.Y.-State-of-Mind,-Pt.-II-Eric-B.-%26-Rakim-Mahogany/" title="Nas's "><img loading="lazy" src="/static/track_images_100/mr16478_20101114_231410204378.jpg" srcset="/static/track_images_100/mr16478_20101114_231410204378.jpg 1x, /static/track_images_200/lr16478_20101114_231410204378.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/68582/Nas-N.Y.-State-of-Mind,-Pt.-II-Eric-B.-%26-Rakim-Mahogany/">Nas's N.Y. State of Mind, Pt. II <span class="sampleType">sample of</span> Eric B. &amp; Rakim's Mahogany</a></span>
</li>
<li class="listEntry sampleCompactEntry">
<a href="/sample/187157/Pro-Era-The-Renaissance-Nas-N.Y.-State-of-Mind/" title="Pro Era's "><img loading="lazy" src="/static/track_images_100/mr10179_20121226_22632873709.jpg" srcset="/static/track_images_100/mr10179_20121226_22632873709.jpg 1x, /static/track_images_200/lr10179_20121226_22632873709.jpg 2x" width="80" height="80"></a>
<span class="connectionTitle"><a href="/sample/187157/Pro-Era-The-Renaissance-Nas-N.Y.-State-of-Mind/">Pro Era's The Renaissance <span class="sampleType">sample of</span> Nas's N.Y. State of Mind</a></span>
</li>
</ul>
</div>
<div class="sidebar-container">
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-top">
<div id="cmn-aside_0">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect_sidebar', 'cmn-aside_0']]);
        </script>
<p id="PrimisSidebarPlaceholder" style="width:0px;height:0px;"></p>
<div id="lazyload-primis-sidebar" width="100%"></div>
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-bottom">
<div id="cmn-feed-inline_-side1">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect', 'cmn-feed-inline_-side1']]);
        </script>
</div>
</div>
</div>
</main>
<footer id="footer" class="footer">
<div class="footerInner">
<div class="sections-wrapper">
<section class="footerAbout footer-section">
<span class="footer-title">About Us</span>
<ul>
<li><a href="/about/">About Us</a></li>
<li><a href="/faq/">FAQs</a></li>
<li><a href="/privacy/">Privacy Policy</a></li>
<li><a href="/terms/">Terms and Conditions</a></li>
</ul>
</section>
<section class="footerCommunity footer-section">
<span class="footer-title">Community</span>
<ul>
<li><a href="/forum/" id="forumFooterLink">Forum</a></li>
<li><a href="/browse/top_contributors/">Top Contributors</a></li>
<li><a href="/browse/facts/">Latest Facts and Stories</a></li>
<li><a href="/browse/latest_comments/">Latest Comments</a></li>
<li><a href="/browse/users/">Members</a></li>
</ul>
</section>
<section class="footerContact footer-section">
<span class="footer-title">Contact</span>
<ul>
<li><a href="/contact/ask/">Contact Us</a></li>
<li><a href="/jobs/">Jobs</a></li>
<li><a href="/copyright/">Copyright / DMCA</a></li>
</ul>
<ul class="social">
<li><a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.youtube.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on YouTube"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 257.567 262.185"><g transform="translate(-239 -327.79)"><ellipse style="isolation: auto; mix-blend-mode: normal; --darkreader-inline-color: #e8e6e3; --darkreader-inline-fill: #181a1b;" cx="367.784" cy="458.883" rx="128.784" ry="131.092" color="#000" overflow="visible" fill="#fff" fill-rule="evenodd" data-darkreader-inline-color="" data-darkreader-inline-fill=""></ellipse><path d="M450.057 419.717c-1.992-7.578-7.857-13.545-15.305-15.572-13.499-3.679-67.631-3.679-67.631-3.679s-54.132 0-67.632 3.68c-7.448 2.026-13.314 7.994-15.305 15.571-3.617 13.737-3.617 42.394-3.617 42.394s0 28.658 3.617 42.394c1.992 7.578 7.857 13.546 15.305 15.571 13.5 3.68 67.632 3.68 67.632 3.68s54.132 0 67.631-3.68c7.448-2.025 13.314-7.993 15.305-15.571 3.617-13.737 3.617-42.394 3.617-42.394s0-28.657-3.617-42.394" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M349.416 488.13l45.244-26.018-45.244-26.02v52.038z" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></g></svg></a></li>
<li><a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.mixcloud.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Mixcloud"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.043 22.013c-.138 0-.278-.04-.403-.122-.333-.222-.422-.674-.198-1.007.67-1 1.024-2.17 1.024-3.386 0-1.216-.354-2.387-1.024-3.387-.224-.332-.135-.784.198-1.007.333-.223.784-.134 1.007.198.83 1.242 1.27 2.692 1.27 4.197 0 1.504-.44 2.955-1.27 4.195-.14.21-.37.32-.604.32" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M23.967 20.835c-.14 0-.28-.04-.406-.125-.33-.225-.417-.677-.192-1.01.442-.65.675-1.413.675-2.203 0-.79-.234-1.552-.675-2.206-.225-.33-.138-.782.194-1.007.332-.225.783-.137 1.008.195.605.894.925 1.938.925 3.02 0 1.08-.32 2.124-.926 3.018-.14.207-.37.32-.603.32M19.875 19.284H9.957c-1.335 0-2.42-1.083-2.42-2.415 0-1.333 1.085-2.417 2.42-2.417.648 0 1.256.25 1.712.708.284.285.743.285 1.027 0 .283-.282.283-.742 0-1.026-.5-.5-1.115-.84-1.783-1.01.69-1.514 2.218-2.524 3.925-2.524 2.376 0 4.31 1.93 4.31 4.303 0 .462-.073.915-.216 1.347-.127.38.08.792.46.918.075.025.152.037.23.037.303 0 .586-.193.687-.498.096-.285.167-.577.215-.874.668.26 1.142.907 1.142 1.664 0 .985-.803 1.787-1.792 1.787zm.698-4.95c-.286-2.907-2.748-5.186-5.734-5.186-2.474 0-4.664 1.588-5.452 3.9-1.866.276-3.305 1.882-3.305 3.82 0 2.133 1.74 3.868 3.874 3.868h9.918c1.79 0 3.245-1.453 3.245-3.24 0-1.546-1.093-2.84-2.547-3.16" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
</ul>
</section>
<section class="footerPartners footer-section">
<span class="footer-title">Partners</span>
<ul>
<li><a href="/metadata/" target="_blank" rel="noopener">Metadata / API</a></li>
<li><a href="/metadata/#customers" target="_blank" rel="noopener">Customers</a></li>
<li><a href="/apps/">App Gallery</a></li>
</ul>
</section>
<section class="footerSitemaps footer-section">
<span class="footer-title">Sitemaps</span>
<ul>
<li><a href="/sitemap/artist/A/">Artists</a></li>
<li><a href="/sitemap/track/A/">Tracks</a></li>
<li><a href="/sitemap/sample/A/">Samples</a></li>
<li><a href="/sitemap/cover/A/">Covers</a></li>
<li><a href="/sitemap/remix/A/">Remixes</a></li>
</ul>
</section>
</div>
<p class="footer-copyright">Copyright © 2022 WhoSampled.com Limited. All rights reserved.</p>
</div>
</footer>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="/static/js/main.js?512716070721"></script>
<script>
      $('.top-menu-avatar').on('click touchstart', function (evt) {
        evt.preventDefault();
        evt.stopPropagation();
        $('#top-menu-dropdown').toggleClass('open');
      });

      $('#top-menu-dropdown, .downloadDropdown, .buyDropdown').on('click touchstart', function (evt) {
        evt.stopPropagation();
      });

      $('html').on('click touchstart', function () {
        $('.downloadDropdown, .buyDropdown').hide();
        $('#top-menu-dropdown').removeClass('open');
      });
    </script>
<script src="https://cdn.jsdelivr.net/npm/vanilla-lazyload@17.4.0/dist/lazyload.min.js"></script>
<script>
        function load_primis_sidebar() {
            if (!window.PrimisSidebarLoaded) {
                var mElmt, primisElmt = document.createElement('script');
                primisElmt.setAttribute('type', 'text/javascript');
                primisElmt.setAttribute('async','async');
                primisElmt.setAttribute('src', 'https://live.primis.tech/live/liveView.php?s=107513');
                mElmt = document.getElementById('PrimisSidebarPlaceholder');
                if (mElmt) {
                    mElmt.parentNode.insertBefore(primisElmt, mElmt.nextSibling);
                    mElmt.parentNode.removeChild(mElmt);
                }
                window.PrimisSidebarLoaded = true;
            }
        }

        var lazyLoadInstancePrimisSidebar = new LazyLoad({
            elements_selector: "#lazyload-primis-sidebar",
            callback_enter: load_primis_sidebar
        });
    </script>
<script>(function(){var js = "window['__CF$cv$params']={r:'741d1509aa0ac03f',m:'mjg78B_swYqF2BpY0jydPNyVWA9a3GiKf_3lnfAVhmU-1661690078-0-AWG3Cb2EwzkUC2T+9Y6zOdnXYTt6KsycbGFqG6+zsVuxYPDZD9EaYjs9IXmBqlpG6thxdW5wKmzifbaA9X2zfWQjyTik50hx1bnoN06UpB6TGqJZmVWwMIn2w97lQGBoTVPTS+bhTCgFscC6OV9IShc=',s:[0x53a72516cc,0x8d30a6fb4d],u:'/cdn-cgi/challenge-platform/h/b'};var now=Date.now()/1000,offset=14400,ts=''+(Math.floor(now)-Math.floor(now%offset)),_cpo=document.createElement('script');_cpo.nonce='',_cpo.src='/cdn-cgi/challenge-platform/h/b/scripts/alpha/invisible.js?ts='+ts,document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = '';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[0].appendChild(_0xj);}}if (document.readyState !== 'loading') {handler();} else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);} else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();}};}})();</script><iframe style="position: absolute; top: 0px; left: 0px; border: medium none; visibility: hidden; --darkreader-inline-border-top: currentcolor; --darkreader-inline-border-right: currentcolor; --darkreader-inline-border-bottom: currentcolor; --darkreader-inline-border-left: currentcolor;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" width="1" height="1"></iframe>

</body>
"""

test_search_page_not_found = """
<body>
<div class="ad-slot">
<div class="top-ad ">
<div id="cmn-leaderboard" class="fw_whosampled">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['top', 'cmn-leaderboard']]);
        </script>
<div id="cmn_wrap">
<header id="header">
<div class="nav" id="js-nav">
<div class="nav-wrap">
<div class="logo-wrapper">
<a href="/" class="logo" aria-label="WhoSampled logo"></a>
</div>
<div class="nav-top">
<div class="socialMedia nav-top-social">
<a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
</div>
<nav class="userLinks nav-top-user">
<div class="nav-inner">
<div class="signin-wrapper mobile">
<a href="/user/login/" rel="nofollow" class="avatar">
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M18 22.082v-1.649c2.203-1.241 4-4.337 4-7.432 0-4.971 0-9-6-9s-6 4.029-6 9c0 3.096 1.797 6.191 4 7.432v1.649C7.216 22.637 2 25.97 2 30h28c0-4.03-5.216-7.364-12-7.918z"></path></svg>
</a>
</div>
<div class="signin-wrapper desktop">
<a href="/user/registration/" rel="nofollow" class="btn signup">Sign up</a> <a href="/user/login/" rel="nofollow" class="btn signin">Sign in</a>
</div>
</div>
</nav>
</div>
<div class="nav-main">
<nav class="nav-links">
<ul>
<li><a href="/news/">News</a></li>
<li><a href="/browse/">Browse</a></li>
<li><a href="/charts/">Charts</a></li>
<li class="nav-submit"><a href="/submit/" class="loginButton">Submit</a></li>
<li><a href="/six-degrees/">6º Game</a></li>
</ul>
</nav>
<form action="/search/" method="get" id="search-bar" class="searchForm nav-search">
<input type="text" id="searchInput" class="searchInput text" name="q" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="none" placeholder="Track, Artist, Movie, TV show" value="some I cant find" maxlength="80" aria-label="Type any track, artist, movie or TV show">
<span class="loading" style="display:none"></span>
<span class="submit-wrapper"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M31.008 27.231l-7.58-6.447c-.784-.705-1.622-1.029-2.299-.998a11.954 11.954 0 0 0 2.87-7.787c0-6.627-5.373-12-12-12s-12 5.373-12 12 5.373 12 12 12c2.972 0 5.691-1.081 7.787-2.87-.031.677.293 1.515.998 2.299l6.447 7.58c1.104 1.226 2.907 1.33 4.007.23s.997-2.903-.23-4.007zM12 20a8 8 0 1 1 0-16 8 8 0 0 1 0 16z"></path></svg><input type="submit" class="submit" value="" aria-label="Search"></span>
</form>
</div>
</div>
</div>
</header>
<main role="main" id="container" class="main-container">
<div id="searchDropdown" class="dropdown search-dropdown" style="display:none">
<div id="searchArtists">
<span class="searchType">Artists</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTracks">
<span class="searchType">Tracks</span>
<ul class="searchList">
</ul>
</div>
<div id="searchMovies">
<span class="searchType">Movies</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTVShows">
<span class="searchType">TV Shows</span>
<ul class="searchList">
</ul>
</div>
</div>
<div class="spSlot">
<a href="/mobile-app/get/" target="_blank" rel="noopener">
<picture>
<source type="image/avif" srcset="/static/images/banners/app-banner-desktop-1100x131.avif 1x, /static/images/banners/app-banner-desktop-2200x261.avif 2x">
<source type="image/webp" srcset="/static/images/banners/app-banner-desktop-1100x131.webp 1x, /static/images/banners/app-banner-desktop-2200x261.webp 2x">
<img src="/static/images/banners/app-banner-desktop-1100x131.jpg" srcset="/static/images/banners/app-banner-desktop-1100x131.jpg 1x, /static/images/banners/app-banner-desktop-2200x261.jpg 2x" width="1100" height="131">
</picture>
</a>
</div>
<div id="content">
<div class="divided-layout search-results">
<div class="leftContent">
<h1 class="headTitle">Search Results for “some I cant find”</h1>
<p style="margin-bottom:2rem">No results for your search “<em>some I cant find</em>”</p>
<div class="ad-slot">
<div class="side-ad ">
<div id="cmn-feed-inline_-n1">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['incontent', 'cmn-feed-inline_-n1']]);
        </script>
</div>
<div class="sidebar-container">
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-top">
<div id="cmn-aside_0">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect_sidebar', 'cmn-aside_0']]);
        </script>
<p id="PrimisSidebarPlaceholder" style="width:0px;height:0px;"></p>
<div id="lazyload-primis-sidebar" width="100%"></div>
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-bottom">
<div id="cmn-feed-inline_-side1">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect', 'cmn-feed-inline_-side1']]);
        </script>
</div>
</div>
</div>
</main>
<footer id="footer" class="footer">
<div class="footerInner">
<div class="sections-wrapper">
<section class="footerAbout footer-section">
<span class="footer-title">About Us</span>
<ul>
<li><a href="/about/">About Us</a></li>
<li><a href="/faq/">FAQs</a></li>
<li><a href="/privacy/">Privacy Policy</a></li>
<li><a href="/terms/">Terms and Conditions</a></li>
</ul>
</section>
<section class="footerCommunity footer-section">
<span class="footer-title">Community</span>
<ul>
<li><a href="/forum/" id="forumFooterLink">Forum</a></li>
<li><a href="/browse/top_contributors/">Top Contributors</a></li>
<li><a href="/browse/facts/">Latest Facts and Stories</a></li>
<li><a href="/browse/latest_comments/">Latest Comments</a></li>
<li><a href="/browse/users/">Members</a></li>
</ul>
</section>
<section class="footerContact footer-section">
<span class="footer-title">Contact</span>
<ul>
<li><a href="/contact/ask/">Contact Us</a></li>
<li><a href="/jobs/">Jobs</a></li>
<li><a href="/copyright/">Copyright / DMCA</a></li>
</ul>
<ul class="social">
<li><a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.youtube.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on YouTube"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 257.567 262.185"><g transform="translate(-239 -327.79)"><ellipse style="isolation: auto; mix-blend-mode: normal; --darkreader-inline-color: #e8e6e3; --darkreader-inline-fill: #181a1b;" cx="367.784" cy="458.883" rx="128.784" ry="131.092" color="#000" overflow="visible" fill="#fff" fill-rule="evenodd" data-darkreader-inline-color="" data-darkreader-inline-fill=""></ellipse><path d="M450.057 419.717c-1.992-7.578-7.857-13.545-15.305-15.572-13.499-3.679-67.631-3.679-67.631-3.679s-54.132 0-67.632 3.68c-7.448 2.026-13.314 7.994-15.305 15.571-3.617 13.737-3.617 42.394-3.617 42.394s0 28.658 3.617 42.394c1.992 7.578 7.857 13.546 15.305 15.571 13.5 3.68 67.632 3.68 67.632 3.68s54.132 0 67.631-3.68c7.448-2.025 13.314-7.993 15.305-15.571 3.617-13.737 3.617-42.394 3.617-42.394s0-28.657-3.617-42.394" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M349.416 488.13l45.244-26.018-45.244-26.02v52.038z" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></g></svg></a></li>
<li><a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.mixcloud.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Mixcloud"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.043 22.013c-.138 0-.278-.04-.403-.122-.333-.222-.422-.674-.198-1.007.67-1 1.024-2.17 1.024-3.386 0-1.216-.354-2.387-1.024-3.387-.224-.332-.135-.784.198-1.007.333-.223.784-.134 1.007.198.83 1.242 1.27 2.692 1.27 4.197 0 1.504-.44 2.955-1.27 4.195-.14.21-.37.32-.604.32" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M23.967 20.835c-.14 0-.28-.04-.406-.125-.33-.225-.417-.677-.192-1.01.442-.65.675-1.413.675-2.203 0-.79-.234-1.552-.675-2.206-.225-.33-.138-.782.194-1.007.332-.225.783-.137 1.008.195.605.894.925 1.938.925 3.02 0 1.08-.32 2.124-.926 3.018-.14.207-.37.32-.603.32M19.875 19.284H9.957c-1.335 0-2.42-1.083-2.42-2.415 0-1.333 1.085-2.417 2.42-2.417.648 0 1.256.25 1.712.708.284.285.743.285 1.027 0 .283-.282.283-.742 0-1.026-.5-.5-1.115-.84-1.783-1.01.69-1.514 2.218-2.524 3.925-2.524 2.376 0 4.31 1.93 4.31 4.303 0 .462-.073.915-.216 1.347-.127.38.08.792.46.918.075.025.152.037.23.037.303 0 .586-.193.687-.498.096-.285.167-.577.215-.874.668.26 1.142.907 1.142 1.664 0 .985-.803 1.787-1.792 1.787zm.698-4.95c-.286-2.907-2.748-5.186-5.734-5.186-2.474 0-4.664 1.588-5.452 3.9-1.866.276-3.305 1.882-3.305 3.82 0 2.133 1.74 3.868 3.874 3.868h9.918c1.79 0 3.245-1.453 3.245-3.24 0-1.546-1.093-2.84-2.547-3.16" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
</ul>
</section>
<section class="footerPartners footer-section">
<span class="footer-title">Partners</span>
<ul>
<li><a href="/metadata/" target="_blank" rel="noopener">Metadata / API</a></li>
<li><a href="/metadata/#customers" target="_blank" rel="noopener">Customers</a></li>
<li><a href="/apps/">App Gallery</a></li>
</ul>
</section>
<section class="footerSitemaps footer-section">
<span class="footer-title">Sitemaps</span>
<ul>
<li><a href="/sitemap/artist/A/">Artists</a></li>
<li><a href="/sitemap/track/A/">Tracks</a></li>
<li><a href="/sitemap/sample/A/">Samples</a></li>
<li><a href="/sitemap/cover/A/">Covers</a></li>
<li><a href="/sitemap/remix/A/">Remixes</a></li>
</ul>
</section>
</div>
<p class="footer-copyright">Copyright © 2022 WhoSampled.com Limited. All rights reserved.</p>
</div>
</footer>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="/static/js/main.js?512716070721"></script>
<script>
      $('.top-menu-avatar').on('click touchstart', function (evt) {
        evt.preventDefault();
        evt.stopPropagation();
        $('#top-menu-dropdown').toggleClass('open');
      });

      $('#top-menu-dropdown, .downloadDropdown, .buyDropdown').on('click touchstart', function (evt) {
        evt.stopPropagation();
      });

      $('html').on('click touchstart', function () {
        $('.downloadDropdown, .buyDropdown').hide();
        $('#top-menu-dropdown').removeClass('open');
      });
    </script>
<script src="https://cdn.jsdelivr.net/npm/vanilla-lazyload@17.4.0/dist/lazyload.min.js"></script>
<script>
        function load_primis_sidebar() {
            if (!window.PrimisSidebarLoaded) {
                var mElmt, primisElmt = document.createElement('script');
                primisElmt.setAttribute('type', 'text/javascript');
                primisElmt.setAttribute('async','async');
                primisElmt.setAttribute('src', 'https://live.primis.tech/live/liveView.php?s=107513');
                mElmt = document.getElementById('PrimisSidebarPlaceholder');
                if (mElmt) {
                    mElmt.parentNode.insertBefore(primisElmt, mElmt.nextSibling);
                    mElmt.parentNode.removeChild(mElmt);
                }
                window.PrimisSidebarLoaded = true;
            }
        }

        var lazyLoadInstancePrimisSidebar = new LazyLoad({
            elements_selector: "#lazyload-primis-sidebar",
            callback_enter: load_primis_sidebar
        });
    </script>


</body>
"""


test_samples_page = """
<body>
<div class="ad-slot">
<div class="top-ad ">
<div id="cmn-leaderboard" class="fw_whosampled">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['top', 'cmn-leaderboard']]);
        </script>
<div id="cmn_wrap">
<header id="header">
<div class="nav" id="js-nav">
<div class="nav-wrap">
<div class="logo-wrapper">
<a href="/" class="logo" aria-label="WhoSampled logo"></a>
</div>
<div class="nav-top">
<div class="socialMedia nav-top-social">
<a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
</div>
<nav class="userLinks nav-top-user">
<div class="nav-inner">
<div class="signin-wrapper mobile">
<a href="/user/login/" rel="nofollow" class="avatar">
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M18 22.082v-1.649c2.203-1.241 4-4.337 4-7.432 0-4.971 0-9-6-9s-6 4.029-6 9c0 3.096 1.797 6.191 4 7.432v1.649C7.216 22.637 2 25.97 2 30h28c0-4.03-5.216-7.364-12-7.918z"></path></svg>
</a>
</div>
<div class="signin-wrapper desktop">
<a href="/user/registration/" rel="nofollow" class="btn signup">Sign up</a> <a href="/user/login/" rel="nofollow" class="btn signin">Sign in</a>
</div>
</div>
</nav>
</div>
<div class="nav-main">
<nav class="nav-links">
<ul>
<li><a href="/news/">News</a></li>
<li><a href="/browse/">Browse</a></li>
<li><a href="/charts/">Charts</a></li>
<li class="nav-submit"><a href="/submit/" class="loginButton">Submit</a></li>
<li><a href="/six-degrees/">6º Game</a></li>
</ul>
</nav>
<form action="/search/" method="get" id="search-bar" class="searchForm nav-search">
<input type="text" id="searchInput" class="searchInput text" name="q" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="none" placeholder="Track, Artist, Movie, TV show" value="" maxlength="80" aria-label="Type any track, artist, movie or TV show">
<span class="loading" style="display:none"></span>
<span class="submit-wrapper"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M31.008 27.231l-7.58-6.447c-.784-.705-1.622-1.029-2.299-.998a11.954 11.954 0 0 0 2.87-7.787c0-6.627-5.373-12-12-12s-12 5.373-12 12 5.373 12 12 12c2.972 0 5.691-1.081 7.787-2.87-.031.677.293 1.515.998 2.299l6.447 7.58c1.104 1.226 2.907 1.33 4.007.23s.997-2.903-.23-4.007zM12 20a8 8 0 1 1 0-16 8 8 0 0 1 0 16z"></path></svg><input type="submit" class="submit" value="" aria-label="Search"></span>
</form>
</div>
</div>
</div>
</header>
<main role="main" id="container" class="main-container">
<div id="searchDropdown" class="dropdown search-dropdown" style="display:none">
<div id="searchArtists">
<span class="searchType">Artists</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTracks">
<span class="searchType">Tracks</span>
<ul class="searchList">
</ul>
</div>
<div id="searchMovies">
<span class="searchType">Movies</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTVShows">
<span class="searchType">TV Shows</span>
<ul class="searchList">
</ul>
</div>
</div>
<div class="spSlot">
<a href="/mobile-app/get/" target="_blank" rel="noopener">
<picture>
<source type="image/avif" srcset="/static/images/banners/app-banner-desktop-1100x131.avif 1x, /static/images/banners/app-banner-desktop-2200x261.avif 2x">
<source type="image/webp" srcset="/static/images/banners/app-banner-desktop-1100x131.webp 1x, /static/images/banners/app-banner-desktop-2200x261.webp 2x">
<img src="/static/images/banners/app-banner-desktop-1100x131.jpg" srcset="/static/images/banners/app-banner-desktop-1100x131.jpg 1x, /static/images/banners/app-banner-desktop-2200x261.jpg 2x" width="1100" height="131">
</picture>
</a>
</div>
<div id="content">
<div class="divided-layout" itemscope="" itemtype="http://schema.org/MusicRecording">
<div class="leftContent">
<div class="shareButtons">
<div class="shareIcons">
<a class="shareFacebook" href="/share/FE+1562/" title="Share on Facebook" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 455.73 455.73"><path d="M0 0v455.73h242.704V279.69h-59.33v-71.863h59.33v-60.353C242.704 103.58 278.286 68 322.18 68h62.024v64.62h-44.382c-13.947 0-25.254 11.308-25.254 25.255v49.953h68.52l-9.47 71.864h-59.05V455.73H455.73V0H0z" fill="#3A559F" style="--darkreader-inline-fill: #7aa1cf;" data-darkreader-inline-fill=""></path></svg>
</a>
<a class="shareTwitter" href="/share/TE+1562/" title="Tweet this page" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 455.731 455.731"><path fill="#50ABF1" d="M0 0h455.73v455.73H0z" style="--darkreader-inline-fill: #55aff1;" data-darkreader-inline-fill=""></path><path d="M60.377 337.822c30.33 19.236 66.308 30.368 104.875 30.368 108.35 0 196.18-87.84 196.18-196.18 0-2.705-.057-5.39-.16-8.067 3.918-3.084 28.156-22.51 34.097-35 0 0-19.684 8.18-38.948 10.107-.038 0-.085.01-.123.01 0 0 .037-.02.103-.067 1.775-1.186 26.59-18.08 29.95-38.207 0 0-13.92 7.43-33.414 13.932a223.675 223.675 0 0 1-10.09 3.103c-12.564-13.41-30.424-21.78-50.25-21.78-38.026 0-68.84 30.806-68.84 68.804 0 5.362.617 10.58 1.784 15.592-5.314-.218-86.237-4.755-141.29-71.423 0 0-32.9 44.917 19.608 91.105 0 0-15.962-.636-29.733-8.864 0 0-5.06 54.416 54.406 68.33 0 0-11.7 4.43-30.368 1.27 0 0 10.44 43.97 63.27 48.078 0 0-41.776 37.74-101.08 28.885l.02.005z" fill="#FFF" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></svg>
</a>
<a class="shareMail" href="mailto:?subject=Interesting%20track%20on%20WhoSampled&amp;body=Hi,%0A%0ACheck%20out%20N.Y.%20State%20of%20Mind%20by%20Nas%20on%20WhoSampled:%0A%0Ahttps://www.whosampled.com/Nas/N.Y.-State-of-Mind/" title="Share via email"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" class="mail2"><path d="M26.666 0H5.334C3.93 0-.006.007-.006.007S0 3.803 0 5.333v21.333c0 1.396.04 5.344.04 5.344S3.795 32 5.333 32h21.332l5.345.003S32 27.976 32 26.666V5.333c0-1.49.01-5.322.01-5.322S28.11 0 26.667 0zM8 8h16c.286 0 .563.06.817.177L16 18.463 7.183 8.176C7.437 8.06 7.713 8 8 8zM6 22V10c0-.042.002-.084.004-.125l5.864 6.842-5.8 5.8c-.046-.17-.07-.342-.07-.517zm18 2H8c-.177 0-.35-.024-.517-.07l5.69-5.69L16 21.537l2.826-3.297 5.69 5.69c-.166.046-.34.07-.516.07zm2-2c0 .177-.024.35-.07.517l-5.8-5.8 5.865-6.842c.003.04.004.083.004.125v12z"></path></svg>
</a>
</div>
</div>
<div class="premium-btn-wrapper">
<a href="/subscription/premium/" class="premium-btn"><span class="mobile-text">GET AD-FREE WHOSAMPLED PREMIUM!</span><span class="desktop-text">GO AD-FREE WITH WHOSAMPLED PREMIUM!</span></a>
</div>
<section class="trackWrap">
<div class="trackImage">
<a href="/Nas/N.Y.-State-of-Mind/">
<img loading="lazy" src="/static/track_images_100/mr148_20081126_03253972786.jpg" srcset="/static/track_images_100/mr148_20081126_03253972786.jpg 1x, /static/track_images_200/lr148_20081126_03253972786.jpg 2x" alt="Nas's N.Y. State of Mind" width="100" height="100">
<meta itemprop="image" content="/static/track_images_200/lr148_20081126_03253972786.jpg">
</a>
</div>
<div class="trackInfo">
<div class="buyDropdownWrap">
<a href="#" class="button downloadButton trackBuyButton" id="trackBuyButton">Buy this Track<span></span></a>
<div class="dropdown downloadDropdown" id="trackBuyDropdown" style="display:none">
<ul>
<li class="d-itunes"><a href="/buy/IK156+1562/" target="_blank" rel="noopener"></a></li>
<li class="d-amazon"><a href="/buy/ZK156+1562/" target="_blank" rel="noopener"></a></li>
<li class="b-ebay"><a href="/buy/EK156+1562/" target="_blank" rel="noopener"></a></li>
<li class="b-amazon"><a href="/buy/OK156+1562/" target="_blank" rel="noopener"></a></li>
</ul>
</div>
</div>
<h1>
Tracks Sampled in <a href="/Nas/N.Y.-State-of-Mind/">N.Y. State of Mind</a><meta itemprop="name" content="N.Y. State of Mind"><br>
<span class="trackArtistNames" itemprop="byArtist" itemscope="" itemtype="http://www.schema.org/MusicGroup">
by <a href="/Nas/">Nas</a>
<meta itemprop="name" content="Nas">
<meta itemprop="url" content="/Nas/">
</span>
</h1>
<meta itemprop="url" content="/Nas/N.Y.-State-of-Mind/">
<meta itemprop="duration" content="PT0H4M56S">
<div class="metainfo-wrapper">
<div class="trackReleaseDetails" itemprop="inAlbum" itemscope="" itemtype="http://www.schema.org/MusicAlbum">
<h3 class="release-name" itemprop="name"><a href="/album/Nas/Illmatic/" itemprop="url">Illmatic</a></h3>
<h3 class="label-details" itemprop="albumRelease" itemscope="" itemtype="http://www.schema.org/MusicRelease"><span itemprop="recordLabel">Columbia</span> <a href="/browse/year/1994/">1994</a><meta itemprop="datePublished" content="1994"></h3>
<div class="track-metainfo">Producer:
<h3>
<span itemprop="producer" itemscope="" itemtype="http://www.schema.org/Person"><span itemprop="name"><a itemprop="url" href="/DJ-Premier/">DJ Premier</a></span></span>
</h3>
</div>
</div>
<div class="tonefuse-desktop">
<div class="tonefuse-ad">
<script>
        /* TFP - Whosampled - Main Tag */
        (function () {
            var opts = {
                artist: "Nas",
                song: "N.Y. State of Mind",
                adunit_id: 100000050,
                div_id: "cf_async_" + Math.floor((Math.random() * 999999999))
            };
            document.write('<div id="'+opts.div_id+'"></div>');var c=function(){cf.showAsyncAd(opts)};if(typeof window.cf !== 'undefined')c();else{cf_async=!0;var r=document.createElement("script"),s=document.getElementsByTagName("script")[0];r.async=!0;r.src="//srv.clickfuse.com/showads/showad.js";r.readyState?r.onreadystatechange=function(){if("loaded"==r.readyState||"complete"==r.readyState)r.onreadystatechange=null,c()}:r.onload=c;s.parentNode.insertBefore(r,s)};
        })();
    </script><div id="cf_async_225452462"></div>
</div>
</div>
</div>
</div>
</section>
<div class="innerContent">
<div class="options-menu-wrapper1">
<div class="optionMenuLabel">Sort:</div>
<div class="optionMenu">
<ul>
<li class="activeOption">
<span class="item">Most Popular</span>
</li>
<li>
<a href="/Nas/N.Y.-State-of-Mind/samples/?ob=0">Earliest to Latest</a>
</li>
<li>
<a href="/Nas/N.Y.-State-of-Mind/samples/?ob=1">Latest to Earliest</a>
</li>
<li>
<a href="/Nas/N.Y.-State-of-Mind/samples/?ob=2">Alphabetically</a>
</li>
<li>
<a href="/Nas/N.Y.-State-of-Mind/samples/?ob=3">Latest Additions</a>
</li>
</ul>
</div>
</div>
<section>
<header class="sectionHeader">
<span class="section-header-title">Contains samples of 5 songs</span>
</header>
<div class="list bordered-list">
<div class="listEntry sampleEntry">
<a href="/sample/896/Nas-N.Y.-State-of-Mind-Joe-Chambers-Mind-Rain/" title="Joe Chambers's Mind Rain"><img loading="lazy" src="/static/track_images_100/mr148_20081126_0403545986.jpg" srcset="/static/track_images_100/mr148_20081126_0403545986.jpg 1x, /static/track_images_200/lr148_20081126_0403545986.jpg 2x" alt="Joe Chambers's Mind Rain" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/896/Nas-N.Y.-State-of-Mind-Joe-Chambers-Mind-Rain/" title="Joe Chambers's Mind Rain">Mind Rain</a>
<span class="trackArtist">by <a href="/Joe-Chambers/">Joe Chambers</a> (1977)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Hook / Riff</span><br>
<span class="bottomItem">Jazz / Blues</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/10075/Nas-N.Y.-State-of-Mind-Donald-Byrd-Flight-Time/" title="Donald Byrd's Flight Time"><img loading="lazy" src="/static/track_images_100/mr1783_2009105_01227660378.jpg" srcset="/static/track_images_100/mr1783_2009105_01227660378.jpg 1x, /static/track_images_200/lr1783_2009105_01227660378.jpg 2x" alt="Donald Byrd's Flight Time" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/10075/Nas-N.Y.-State-of-Mind-Donald-Byrd-Flight-Time/" title="Donald Byrd's Flight Time">Flight Time</a>
<span class="trackArtist">by <a href="/Donald-Byrd/">Donald Byrd</a> (1973)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Sound Effect / Other</span><br>
<span class="bottomItem">Jazz / Blues</span>

</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/109933/Nas-N.Y.-State-of-Mind-Kool-%26-the-Gang-N.T./" title="Kool &amp; the Gang's N.T."><img loading="lazy" src="/static/track_images_100/mr11_20081027_16487146808.jpg" srcset="/static/track_images_100/mr11_20081027_16487146808.jpg 1x, /static/track_images_200/lr11_20081027_16487146808.jpg 2x" alt="Kool &amp; the Gang's N.T." width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/109933/Nas-N.Y.-State-of-Mind-Kool-%26-the-Gang-N.T./" title="Kool &amp; the Gang's N.T.">N.T.</a>
<span class="trackArtist">by <a href="/Kool-%26-the-Gang/">Kool &amp; the Gang</a> (1971)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Drums</span><br>
<span class="bottomItem">Soul / Funk / Disco</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/12391/Nas-N.Y.-State-of-Mind-Eric-B.-%26-Rakim-Mahogany/" title="Eric B. &amp; Rakim's Mahogany"><img loading="lazy" src="/static/track_images_100/mr185_20081212_04718658735.jpg" srcset="/static/track_images_100/mr185_20081212_04718658735.jpg 1x, /static/track_images_200/lr185_20081212_04718658735.jpg 2x" alt="Eric B. &amp; Rakim's Mahogany" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/12391/Nas-N.Y.-State-of-Mind-Eric-B.-%26-Rakim-Mahogany/" title="Eric B. &amp; Rakim's Mahogany">Mahogany</a>
<span class="trackArtist">by <a href="/Eric-B.-%26-Rakim/">Eric B. &amp; Rakim</a> (1990)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Vocals / Lyrics</span><br>
<span class="bottomItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/22883/Nas-N.Y.-State-of-Mind-Main-Source-Nas-Joe-Fatal-Akinyele-Live-at-the-Barbeque/" title="Main Source feat. Nas, Joe Fatal and Akinyele's Live at the Barbeque"><img loading="lazy" src="/static/track_images_100/mr3_20081229_223156333382.jpg" srcset="/static/track_images_100/mr3_20081229_223156333382.jpg 1x, /static/track_images_200/lr3_20081229_223156333382.jpg 2x" alt="Main Source feat. Nas, Joe Fatal and Akinyele's Live at the Barbeque" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/22883/Nas-N.Y.-State-of-Mind-Main-Source-Nas-Joe-Fatal-Akinyele-Live-at-the-Barbeque/" title="Main Source feat. Nas, Joe Fatal and Akinyele's Live at the Barbeque">Live at the Barbeque</a>
<span class="trackArtist">by <a href="/Main-Source/">Main Source</a> feat. <a href="/Nas/">Nas</a>, <a href="/Joe-Fatal/">Joe Fatal</a> and <a href="/Akinyele/">Akinyele</a> (1991)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Vocals / Lyrics</span><br>
<span class="bottomItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
</div>
</section>
</div>
</div>
<div class="sidebar-container">
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-top">
<div id="cmn-aside_0">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect_sidebar', 'cmn-aside_0']]);
        </script>
<p id="PrimisSidebarPlaceholder" style="width:0px;height:0px;"></p>
<div id="lazyload-primis-sidebar" width="100%"></div>
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-bottom">
<div id="cmn-feed-inline_-side1">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect', 'cmn-feed-inline_-side1']]);
        </script>
</div>
</div>
</div>
</main>
<footer id="footer" class="footer">
<div class="footerInner">
<div class="sections-wrapper">
<section class="footerAbout footer-section">
<span class="footer-title">About Us</span>
<ul>
<li><a href="/about/">About Us</a></li>
<li><a href="/faq/">FAQs</a></li>
<li><a href="/privacy/">Privacy Policy</a></li>
<li><a href="/terms/">Terms and Conditions</a></li>
</ul>
</section>
<section class="footerCommunity footer-section">
<span class="footer-title">Community</span>
<ul>
<li><a href="/forum/" id="forumFooterLink">Forum</a></li>
<li><a href="/browse/top_contributors/">Top Contributors</a></li>
<li><a href="/browse/facts/">Latest Facts and Stories</a></li>
<li><a href="/browse/latest_comments/">Latest Comments</a></li>
<li><a href="/browse/users/">Members</a></li>
</ul>
</section>
<section class="footerContact footer-section">
<span class="footer-title">Contact</span>
<ul>
<li><a href="/contact/ask/">Contact Us</a></li>
<li><a href="/jobs/">Jobs</a></li>
<li><a href="/copyright/">Copyright / DMCA</a></li>
</ul>
<ul class="social">
<li><a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.youtube.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on YouTube"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 257.567 262.185"><g transform="translate(-239 -327.79)"><ellipse style="isolation: auto; mix-blend-mode: normal; --darkreader-inline-color: #e8e6e3; --darkreader-inline-fill: #181a1b;" cx="367.784" cy="458.883" rx="128.784" ry="131.092" color="#000" overflow="visible" fill="#fff" fill-rule="evenodd" data-darkreader-inline-color="" data-darkreader-inline-fill=""></ellipse><path d="M450.057 419.717c-1.992-7.578-7.857-13.545-15.305-15.572-13.499-3.679-67.631-3.679-67.631-3.679s-54.132 0-67.632 3.68c-7.448 2.026-13.314 7.994-15.305 15.571-3.617 13.737-3.617 42.394-3.617 42.394s0 28.658 3.617 42.394c1.992 7.578 7.857 13.546 15.305 15.571 13.5 3.68 67.632 3.68 67.632 3.68s54.132 0 67.631-3.68c7.448-2.025 13.314-7.993 15.305-15.571 3.617-13.737 3.617-42.394 3.617-42.394s0-28.657-3.617-42.394" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M349.416 488.13l45.244-26.018-45.244-26.02v52.038z" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></g></svg></a></li>
<li><a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.mixcloud.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Mixcloud"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.043 22.013c-.138 0-.278-.04-.403-.122-.333-.222-.422-.674-.198-1.007.67-1 1.024-2.17 1.024-3.386 0-1.216-.354-2.387-1.024-3.387-.224-.332-.135-.784.198-1.007.333-.223.784-.134 1.007.198.83 1.242 1.27 2.692 1.27 4.197 0 1.504-.44 2.955-1.27 4.195-.14.21-.37.32-.604.32" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M23.967 20.835c-.14 0-.28-.04-.406-.125-.33-.225-.417-.677-.192-1.01.442-.65.675-1.413.675-2.203 0-.79-.234-1.552-.675-2.206-.225-.33-.138-.782.194-1.007.332-.225.783-.137 1.008.195.605.894.925 1.938.925 3.02 0 1.08-.32 2.124-.926 3.018-.14.207-.37.32-.603.32M19.875 19.284H9.957c-1.335 0-2.42-1.083-2.42-2.415 0-1.333 1.085-2.417 2.42-2.417.648 0 1.256.25 1.712.708.284.285.743.285 1.027 0 .283-.282.283-.742 0-1.026-.5-.5-1.115-.84-1.783-1.01.69-1.514 2.218-2.524 3.925-2.524 2.376 0 4.31 1.93 4.31 4.303 0 .462-.073.915-.216 1.347-.127.38.08.792.46.918.075.025.152.037.23.037.303 0 .586-.193.687-.498.096-.285.167-.577.215-.874.668.26 1.142.907 1.142 1.664 0 .985-.803 1.787-1.792 1.787zm.698-4.95c-.286-2.907-2.748-5.186-5.734-5.186-2.474 0-4.664 1.588-5.452 3.9-1.866.276-3.305 1.882-3.305 3.82 0 2.133 1.74 3.868 3.874 3.868h9.918c1.79 0 3.245-1.453 3.245-3.24 0-1.546-1.093-2.84-2.547-3.16" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
</ul>
</section>
<section class="footerPartners footer-section">
<span class="footer-title">Partners</span>
<ul>
<li><a href="/metadata/" target="_blank" rel="noopener">Metadata / API</a></li>
<li><a href="/metadata/#customers" target="_blank" rel="noopener">Customers</a></li>
<li><a href="/apps/">App Gallery</a></li>
</ul>
</section>
<section class="footerSitemaps footer-section">
<span class="footer-title">Sitemaps</span>
<ul>
<li><a href="/sitemap/artist/A/">Artists</a></li>
<li><a href="/sitemap/track/A/">Tracks</a></li>
<li><a href="/sitemap/sample/A/">Samples</a></li>
<li><a href="/sitemap/cover/A/">Covers</a></li>
<li><a href="/sitemap/remix/A/">Remixes</a></li>
</ul>
</section>
</div>
<p class="footer-copyright">Copyright © 2022 WhoSampled.com Limited. All rights reserved.</p>
</div>
</footer>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="/static/js/main.js?512716070721"></script>
<script>
      $('.top-menu-avatar').on('click touchstart', function (evt) {
        evt.preventDefault();
        evt.stopPropagation();
        $('#top-menu-dropdown').toggleClass('open');
      });

      $('#top-menu-dropdown, .downloadDropdown, .buyDropdown').on('click touchstart', function (evt) {
        evt.stopPropagation();
      });

      $('html').on('click touchstart', function () {
        $('.downloadDropdown, .buyDropdown').hide();
        $('#top-menu-dropdown').removeClass('open');
      });
    </script>
<script src="https://cdn.jsdelivr.net/npm/vanilla-lazyload@17.4.0/dist/lazyload.min.js"></script>
<script>
        function load_primis_sidebar() {
            if (!window.PrimisSidebarLoaded) {
                var mElmt, primisElmt = document.createElement('script');
                primisElmt.setAttribute('type', 'text/javascript');
                primisElmt.setAttribute('async','async');
                primisElmt.setAttribute('src', 'https://live.primis.tech/live/liveView.php?s=107513');
                mElmt = document.getElementById('PrimisSidebarPlaceholder');
                if (mElmt) {
                    mElmt.parentNode.insertBefore(primisElmt, mElmt.nextSibling);
                    mElmt.parentNode.removeChild(mElmt);
                }
                window.PrimisSidebarLoaded = true;
            }
        }

        var lazyLoadInstancePrimisSidebar = new LazyLoad({
            elements_selector: "#lazyload-primis-sidebar",
            callback_enter: load_primis_sidebar
        });
    </script>
<script>(function(){var js = "window['__CF$cv$params']={r:'7417e3f21f1abc1b',m:'3nRpXDjmSJ8U_7gHJr_WWXJBTmhX2cgSlYsW_RISbQo-1661635638-0-AdwoDtP/U/fFQ6a1LOO28GfbDf/guYX6FTp+NvuTh2L+hMms9wqHlltrQbAsa4PbIIIPkUlCdn2A2YvjLUBwwu5i1+qnlnDawuNQlssy950yyQGuJdioJCwe0Yo5l21bJ0D875UcfLx0/hEjwfVWtuA+Z0WfnIcKi4pWMdZnf50s',s:[0x938725428f,0xba8a7bd7fd],u:'/cdn-cgi/challenge-platform/h/b'};var now=Date.now()/1000,offset=14400,ts=''+(Math.floor(now)-Math.floor(now%offset)),_cpo=document.createElement('script');_cpo.nonce='',_cpo.src='/cdn-cgi/challenge-platform/h/b/scripts/alpha/invisible.js?ts='+ts,document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = '';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[0].appendChild(_0xj);}}if (document.readyState !== 'loading') {handler();} else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);} else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();}};}})();</script><iframe style="position: absolute; top: 0px; left: 0px; border: medium none; visibility: hidden; --darkreader-inline-border-top: currentcolor; --darkreader-inline-border-right: currentcolor; --darkreader-inline-border-bottom: currentcolor; --darkreader-inline-border-left: currentcolor;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" width="1" height="1"></iframe>

</body>
"""

test_track_page = """
<body>
<div class="ad-slot">
<div class="top-ad ">
<div id="cmn-leaderboard" class="fw_whosampled">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['top', 'cmn-leaderboard']]);
        </script>
<div id="cmn_wrap">
<header id="header">
<div class="nav" id="js-nav">
<div class="nav-wrap">
<div class="logo-wrapper">
<a href="/" class="logo" aria-label="WhoSampled logo"></a>
</div>
<div class="nav-top">
<div class="socialMedia nav-top-social">
<a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
<a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a>
</div>
<nav class="userLinks nav-top-user">
<div class="nav-inner">
<div class="signin-wrapper mobile">
<a href="/user/login/" rel="nofollow" class="avatar">
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M18 22.082v-1.649c2.203-1.241 4-4.337 4-7.432 0-4.971 0-9-6-9s-6 4.029-6 9c0 3.096 1.797 6.191 4 7.432v1.649C7.216 22.637 2 25.97 2 30h28c0-4.03-5.216-7.364-12-7.918z"></path></svg>
</a>
</div>
<div class="signin-wrapper desktop">
<a href="/user/registration/" rel="nofollow" class="btn signup">Sign up</a> <a href="/user/login/" rel="nofollow" class="btn signin">Sign in</a>
</div>
</div>
</nav>
</div>
<div class="nav-main">
<nav class="nav-links">
<ul>
<li><a href="/news/">News</a></li>
<li><a href="/browse/">Browse</a></li>
<li><a href="/charts/">Charts</a></li>
<li class="nav-submit"><a href="/submit/" class="loginButton">Submit</a></li>
<li><a href="/six-degrees/">6º Game</a></li>
</ul>
</nav>
<form action="/search/" method="get" id="search-bar" class="searchForm nav-search">
<input type="text" id="searchInput" class="searchInput text" name="q" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="none" placeholder="Track, Artist, Movie, TV show" value="" maxlength="80" aria-label="Type any track, artist, movie or TV show">
<span class="loading" style="display:none"></span>
<span class="submit-wrapper"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M31.008 27.231l-7.58-6.447c-.784-.705-1.622-1.029-2.299-.998a11.954 11.954 0 0 0 2.87-7.787c0-6.627-5.373-12-12-12s-12 5.373-12 12 5.373 12 12 12c2.972 0 5.691-1.081 7.787-2.87-.031.677.293 1.515.998 2.299l6.447 7.58c1.104 1.226 2.907 1.33 4.007.23s.997-2.903-.23-4.007zM12 20a8 8 0 1 1 0-16 8 8 0 0 1 0 16z"></path></svg><input type="submit" class="submit" value="" aria-label="Search"></span>
</form>
</div>
</div>
</div>
</header>
<main role="main" id="container" class="main-container">
<div id="searchDropdown" class="dropdown search-dropdown" style="display:none">
<div id="searchArtists">
<span class="searchType">Artists</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTracks">
<span class="searchType">Tracks</span>
<ul class="searchList">
</ul>
</div>
<div id="searchMovies">
<span class="searchType">Movies</span>
<ul class="searchList">
</ul>
</div>
<div id="searchTVShows">
<span class="searchType">TV Shows</span>
<ul class="searchList">
</ul>
</div>
</div>
<div class="spSlot">
<a href="/mobile-app/get/" target="_blank" rel="noopener">
<picture>
<source type="image/avif" srcset="/static/images/banners/app-banner-desktop-1100x131.avif 1x, /static/images/banners/app-banner-desktop-2200x261.avif 2x">
<source type="image/webp" srcset="/static/images/banners/app-banner-desktop-1100x131.webp 1x, /static/images/banners/app-banner-desktop-2200x261.webp 2x">
<img src="/static/images/banners/app-banner-desktop-1100x131.jpg" srcset="/static/images/banners/app-banner-desktop-1100x131.jpg 1x, /static/images/banners/app-banner-desktop-2200x261.jpg 2x" width="1100" height="131">
</picture>
</a>
</div>
<div id="content">
<div class="divided-layout" itemscope="" itemtype="http://schema.org/MusicRecording">
<div class="leftContent">
<div class="shareButtons">
<div class="shareIcons">
<a class="shareFacebook" href="/share/FK+1226/" title="Share on Facebook" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 455.73 455.73"><path d="M0 0v455.73h242.704V279.69h-59.33v-71.863h59.33v-60.353C242.704 103.58 278.286 68 322.18 68h62.024v64.62h-44.382c-13.947 0-25.254 11.308-25.254 25.255v49.953h68.52l-9.47 71.864h-59.05V455.73H455.73V0H0z" fill="#3A559F" style="--darkreader-inline-fill: #7aa1cf;" data-darkreader-inline-fill=""></path></svg>
</a>
<a class="shareTwitter" href="/share/TK+1226/" title="Tweet this page" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 455.731 455.731"><path fill="#50ABF1" d="M0 0h455.73v455.73H0z" style="--darkreader-inline-fill: #55aff1;" data-darkreader-inline-fill=""></path><path d="M60.377 337.822c30.33 19.236 66.308 30.368 104.875 30.368 108.35 0 196.18-87.84 196.18-196.18 0-2.705-.057-5.39-.16-8.067 3.918-3.084 28.156-22.51 34.097-35 0 0-19.684 8.18-38.948 10.107-.038 0-.085.01-.123.01 0 0 .037-.02.103-.067 1.775-1.186 26.59-18.08 29.95-38.207 0 0-13.92 7.43-33.414 13.932a223.675 223.675 0 0 1-10.09 3.103c-12.564-13.41-30.424-21.78-50.25-21.78-38.026 0-68.84 30.806-68.84 68.804 0 5.362.617 10.58 1.784 15.592-5.314-.218-86.237-4.755-141.29-71.423 0 0-32.9 44.917 19.608 91.105 0 0-15.962-.636-29.733-8.864 0 0-5.06 54.416 54.406 68.33 0 0-11.7 4.43-30.368 1.27 0 0 10.44 43.97 63.27 48.078 0 0-41.776 37.74-101.08 28.885l.02.005z" fill="#FFF" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></svg>
</a>
<a class="shareMail" href="mailto:?subject=Interesting%20track%20on%20WhoSampled&amp;body=Hi,%0A%0ACheck%20out%20Represent%20by%20Nas%20on%20WhoSampled:%0A%0Ahttps://www.whosampled.com/Nas/Represent/" title="Share via email"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" class="mail2"><path d="M26.666 0H5.334C3.93 0-.006.007-.006.007S0 3.803 0 5.333v21.333c0 1.396.04 5.344.04 5.344S3.795 32 5.333 32h21.332l5.345.003S32 27.976 32 26.666V5.333c0-1.49.01-5.322.01-5.322S28.11 0 26.667 0zM8 8h16c.286 0 .563.06.817.177L16 18.463 7.183 8.176C7.437 8.06 7.713 8 8 8zM6 22V10c0-.042.002-.084.004-.125l5.864 6.842-5.8 5.8c-.046-.17-.07-.342-.07-.517zm18 2H8c-.177 0-.35-.024-.517-.07l5.69-5.69L16 21.537l2.826-3.297 5.69 5.69c-.166.046-.34.07-.516.07zm2-2c0 .177-.024.35-.07.517l-5.8-5.8 5.865-6.842c.003.04.004.083.004.125v12z"></path></svg>
</a>
</div>
</div>
<div class="premium-btn-wrapper">
<a href="/subscription/premium/" class="premium-btn"><span class="mobile-text">GET AD-FREE WHOSAMPLED PREMIUM!</span><span class="desktop-text">GO AD-FREE WITH WHOSAMPLED PREMIUM!</span></a>
</div>
<section class="trackWrap">
<div class="trackImage">
<img itemprop="thumbnailUrl" src="/static/track_images_100/mr397_200935_21457912504.jpg" srcset="/static/track_images_100/mr397_200935_21457912504.jpg 1x, /static/track_images_200/lr397_200935_21457912504.jpg 2x" alt="Represent - Nas" width="100" height="100">
<meta itemprop="image" content="/static/track_images_200/lr397_200935_21457912504.jpg">
</div>
<div class="trackInfo">
<div class="buyDropdownWrap">
<a href="#" class="button downloadButton trackBuyButton" id="trackBuyButton">Buy this Track<span></span></a>
<div class="dropdown downloadDropdown" id="trackBuyDropdown" style="display:none">
<ul>
<li class="d-itunes"><a href="/buy/IK156+1226/" target="_blank" rel="noopener"></a></li>
<li class="d-amazon"><a href="/buy/ZK156+1226/" target="_blank" rel="noopener"></a></li>
<li class="b-ebay"><a href="/buy/EK156+1226/" target="_blank" rel="noopener"></a></li>
<li class="b-amazon"><a href="/buy/OK156+1226/" target="_blank" rel="noopener"></a></li>
</ul>
</div>
</div>
<h1>
Represent<meta itemprop="name" content="Represent"><br>
<span class="trackArtistNames" itemprop="byArtist" itemscope="" itemtype="http://www.schema.org/MusicGroup">
by <a href="/Nas/">Nas</a>
<meta itemprop="name" content="Nas">
<meta itemprop="url" content="/Nas/">
</span>
</h1>
<meta itemprop="url" content="/Nas/Represent/">
<meta itemprop="duration" content="PT0H4M15S">
<div class="metainfo-wrapper">
<div class="trackReleaseDetails" itemprop="inAlbum" itemscope="" itemtype="http://www.schema.org/MusicAlbum">
<h3 class="release-name" itemprop="name"><a href="/album/Nas/Illmatic/" itemprop="url">Illmatic</a></h3>
<h3 class="label-details" itemprop="albumRelease" itemscope="" itemtype="http://www.schema.org/MusicRelease"><span itemprop="recordLabel">Columbia</span> <a href="/browse/year/1994/">1994</a><meta itemprop="datePublished" content="1994"></h3>
<div class="track-metainfo">Producer:
<h3>
<span itemprop="producer" itemscope="" itemtype="http://www.schema.org/Person"><span itemprop="name"><a itemprop="url" href="/DJ-Premier/">DJ Premier</a></span></span>
</h3>
</div>
</div>
<div class="tonefuse-desktop">
<div class="tonefuse-ad">
<script>
        /* TFP - Whosampled - Main Tag */
        (function () {
            var opts = {
                artist: "Nas",
                song: "Represent",
                adunit_id: 100000050,
                div_id: "cf_async_" + Math.floor((Math.random() * 999999999))
            };
            document.write('<div id="'+opts.div_id+'"></div>');var c=function(){cf.showAsyncAd(opts)};if(typeof window.cf !== 'undefined')c();else{cf_async=!0;var r=document.createElement("script"),s=document.getElementsByTagName("script")[0];r.async=!0;r.src="//srv.clickfuse.com/showads/showad.js";r.readyState?r.onreadystatechange=function(){if("loaded"==r.readyState||"complete"==r.readyState)r.onreadystatechange=null,c()}:r.onload=c;s.parentNode.insertBefore(r,s)};
        })();
    </script><div id="cf_async_426268585"></div>
</div>
</div>
</div>
</div>
</section>
<div class="media-wrapper">
<div class="media-container track-embed">
<div class="embed-placeholder youtube-placeholder" data-id="xiVY_yPgvMs" data-width="640" data-height="360" data-player-vars="{&quot;modestbranding&quot;: 1, &quot;rel&quot;: 0, &quot;iv_load_policy&quot;: 3}" data-thumbnail-file-name="maxresdefault">
<div class="play-button"></div>
<img src="https://i.ytimg.com/vi/xiVY_yPgvMs/maxresdefault.jpg">
</div>
</div>
</div>
<section class="section track-meta">
<div class="track-meta__el1">
<div class="track-meta__el5">
<span>Main genre</span>: <a href="/genre/Hip-Hop/"><span itemprop="genre">Hip-Hop / Rap / R&amp;B</span></a>
</div>
<div class="track-meta__el5">
<span>Tags</span>: <span itemprop="keywords"><a href="/song-tag/National%20Recording%20Registry/">National Recording Registry</a>, <a href="/song-tag/Sampled%20in%20More%20Than%2030%20Songs/">Sampled in More Than 30 Songs</a> </span>
</div>
</div>
<div class="track-meta__el2">
<div class="track-meta__el3">
<span class="track-meta__el4"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="32" viewBox="0 0 36 32"><path d="M24 24.082v-1.65c2.203-1.24 4-4.336 4-7.43 0-4.972 0-9-6-9s-6 4.028-6 9c0 3.095 1.797 6.19 4 7.43v1.65C13.216 24.637 8 27.97 8 32h28c0-4.03-5.216-7.364-12-7.918z"></path><path d="M10.225 24.854c1.728-1.13 3.877-1.99 6.243-2.513-.47-.555-.897-1.175-1.265-1.843-.95-1.726-1.453-3.627-1.453-5.497 0-2.69 0-5.228.956-7.305.928-2.016 2.598-3.265 4.976-3.734C19.152 1.57 17.746 0 14 0 8 0 8 4.03 8 9c0 3.096 1.797 6.19 4 7.432v1.65c-6.784.554-12 3.887-12 7.917h8.72c.453-.404.955-.788 1.505-1.147z"></path></svg></span> <span><b>47</b> users contributed to this page</span>
</div>
</div>
</section>
<section>
<header class="sectionHeader">
<span class="section-header-title">Contains samples of 2 songs</span>
</header>
<div class="list bordered-list">
<div class="listEntry sampleEntry">
<a href="/sample/2473/Nas-Represent-Lee-Erwin-Thief-of-Bagdad/" title="Lee Erwin's Thief of Bagdad"><img loading="lazy" src="/static/track_images_100/mr32163_2011103_94036720915.jpg" srcset="/static/track_images_100/mr32163_2011103_94036720915.jpg 1x, /static/track_images_200/lr32163_2011103_94036720915.jpg 2x" alt="Lee Erwin's Thief of Bagdad" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/2473/Nas-Represent-Lee-Erwin-Thief-of-Bagdad/" title="Lee Erwin's Thief of Bagdad">Thief of Bagdad</a>
<span class="trackArtist">by <a href="/Lee-Erwin/">Lee Erwin</a> (1974)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Multiple Elements</span><br>
<span class="bottomItem">Soundtrack / Library</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/336429/Nas-Represent-George-Clinton-All-Night-(Drums)/" title="George Clinton's All Night (Drums)"><img loading="lazy" src="/static/track_images_100/mr124551_201541_134039159360.jpg" srcset="/static/track_images_100/mr124551_201541_134039159360.jpg 1x, /static/track_images_200/lr124551_201541_134039159360.jpg 2x" alt="George Clinton's All Night (Drums)" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/336429/Nas-Represent-George-Clinton-All-Night-(Drums)/" title="George Clinton's All Night (Drums)">All Night (Drums)</a>
<span class="trackArtist">by <a href="/George-Clinton/">George Clinton</a> (1993)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Drums</span><br>
<span class="bottomItem">Soul / Funk / Disco</span>
</div>
</div>
</div>
</div>
</section>
<section>
<header class="sectionHeader">
<span class="section-header-title">Was sampled in 36 songs</span>
<a class="moreButton" href="/Nas/Represent/sampled/">see all</a>
</header>
<div class="list bordered-list">
<div class="listEntry sampleEntry">
<a href="/sample/489216/Eminem-Infinite-Nas-Represent/" title="Eminem's Infinite"><img loading="lazy" src="/static/track_images_100/mr9387_201223_4655903334.jpg" srcset="/static/track_images_100/mr9387_201223_4655903334.jpg 1x, /static/track_images_200/lr9387_201223_4655903334.jpg 2x" alt="Eminem's Infinite" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/489216/Eminem-Infinite-Nas-Represent/" title="Eminem's Infinite">Infinite</a>
<span class="trackArtist">by <a href="/Eminem/">Eminem</a> (1996)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Vocals / Lyrics</span><br>
<span class="bottomItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/322542/Fabolous-Velous-Gone-for-the-Winter-Nas-Represent/" title="Fabolous feat. Velous's Gone for the Winter"><img loading="lazy" src="/static/track_images_100/mr5875_20141230_161534725853.jpg" srcset="/static/track_images_100/mr5875_20141230_161534725853.jpg 1x, /static/track_images_200/lr5875_20141230_161534725853.jpg 2x" alt="Fabolous feat. Velous's Gone for the Winter" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/322542/Fabolous-Velous-Gone-for-the-Winter-Nas-Represent/" title="Fabolous feat. Velous's Gone for the Winter">Gone for the Winter</a>
<span class="trackArtist">by <a href="/Fabolous/">Fabolous</a> feat. <a href="/Velous/">Velous</a> (2014)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Vocals / Lyrics</span><br>
<span class="bottomItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/sample/42565/Jay-Z-Rap-Game-Crack-Game-Nas-Represent/" title="Jay-Z's Rap Game / Crack Game"><img loading="lazy" src="/static/track_images_100/mr2370_2010124_182150272712.jpg" srcset="/static/track_images_100/mr2370_2010124_182150272712.jpg 1x, /static/track_images_200/lr2370_2010124_182150272712.jpg 2x" alt="Jay-Z's Rap Game / Crack Game" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/sample/42565/Jay-Z-Rap-Game-Crack-Game-Nas-Represent/" title="Jay-Z's Rap Game / Crack Game">Rap Game / Crack Game</a>
<span class="trackArtist">by <a href="/Jay-Z/">Jay-Z</a> (1997)
</span>
</div>
<div class="trackBadge">
<span class="topItem">Vocals / Lyrics</span><br>
<span class="bottomItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
</div>
</section>
<div class="list-content-action-mobile">
<a href="/Nas/Represent/sampled/" class="btn">see all</a>
</div>
<section>
<header class="sectionHeader">
<span class="section-header-title">Was covered in 5 songs</span>
<a class="moreButton" href="/Nas/Represent/covered/">see all</a>
</header>
<div class="list bordered-list">
<div class="listEntry sampleEntry">
<a href="/cover/96757/Elzhi-Will-Sessions-Represent-Nas-Represent/" title="Elzhi and Will Sessions's Represent"><img loading="lazy" src="/static/track_images_100/mr12352_2011511_161119794856.jpg" srcset="/static/track_images_100/mr12352_2011511_161119794856.jpg 1x, /static/track_images_200/lr12352_2011511_161119794856.jpg 2x" alt="Elzhi and Will Sessions's Represent" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/cover/96757/Elzhi-Will-Sessions-Represent-Nas-Represent/" title="Elzhi and Will Sessions's Represent">Represent</a>
<span class="trackArtist">by <a href="/Elzhi/">Elzhi</a> and <a href="/Will-Sessions/">Will Sessions</a> (2011)
</span>
</div>
<div class="trackBadge">
<div class="oneLabel">
<span class="topItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/cover/397294/Genetikk-Represent-Nas-Represent/" title="Genetikk's Represent"><img loading="lazy" src="/static/track_images_100/mr138990_201555_205717218048.jpg" srcset="/static/track_images_100/mr138990_201555_205717218048.jpg 1x, /static/track_images_200/lr138990_201555_205717218048.jpg 2x" alt="Genetikk's Represent" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/cover/397294/Genetikk-Represent-Nas-Represent/" title="Genetikk's Represent">Represent</a>
<span class="trackArtist">by <a href="/Genetikk/">Genetikk</a> (2013)
</span>
</div>
<div class="trackBadge">
<div class="oneLabel">
<span class="topItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
</div>
<div class="listEntry sampleEntry">
<a href="/cover/66890/Fashawn-Represent-Nas-Represent/" title="Fashawn's Represent"><img loading="lazy" src="/static/track_images_100/mr5875_2010113_32712367989.jpg" srcset="/static/track_images_100/mr5875_2010113_32712367989.jpg 1x, /static/track_images_200/lr5875_2010113_32712367989.jpg 2x" alt="Fashawn's Represent" width="80" height="80"></a>
<div class="trackDetails">
<div class="details-inner">
<a class="trackName playIcon" href="/cover/66890/Fashawn-Represent-Nas-Represent/" title="Fashawn's Represent">Represent</a>
<span class="trackArtist">by <a href="/Fashawn/">Fashawn</a> (2010)
</span>
</div>
<div class="trackBadge">
<div class="oneLabel">
<span class="topItem">Hip-Hop / Rap / R&amp;B</span>
</div>
</div>
</div>
</div>
</div>
</section>
<div class="list-content-action-mobile">
<a href="/Nas/Represent/covered/" class="btn">see all</a>
</div>
<section id="fs-wrapper" class="fs-wrapper">
<header class="fs-header">
<h2 class="headTitle">Facts and Stories</h2>
</header>
<div class="fs-list">
<article id="fact-6024" class="fs-entry-wrapper">
<section class="fs-entry">
<div class="fs-entry__left">
<div class="fs-votes">
<a href="/user/login/?next=/Nas/Represent/" class="fs-vote-up " data-fact-id="6024"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 1l-15 15h9v16h12v-16h9z"></path></svg>
</a> <span class="fs-votes-count">2</span> <a href="/user/login/?next=/Nas/Represent/" class="fs-vote-down " data-fact-id="6024"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 31l15-15h-9v-16h-12v16h-9z"></path></svg>
</a>
</div>
</div>
<div class="fs-entry__right">
<section class="fs-entry-content" style="">
<p>In episode #6 of <a class="js-artist" data-artist-id="2319" data-artist-name="DJ Premier" data-linked="true" href="/DJ-Premier/">DJ Premier</a>'s 'So Wassup?' video series, Premier explains that the well known album version of 'Represent' is in fact a remix. Nas recorded the vocal to a different, jazzier instrumental originally, but Premier created a new version after hearing (and being impressed by) draft material for the album produced by <a class="js-artist" data-artist-id="650" data-artist-name="Q-Tip" data-linked="true" href="/Q-Tip/">Q-Tip</a> and <a class="js-artist" data-artist-id="2484" data-artist-name="Large Professor" data-linked="true" href="/Large-Professor/">Large Professor</a>. The track was originally titled 'Representin'.</p>
<p></p><div class="media-wrapper youtube-embed" data-youtube-id="FpQ0yWA-oNQ">
<div class="media-container">
<div class="embed-placeholder youtube-placeholder" data-height="360" data-id="FpQ0yWA-oNQ" data-player-vars="{&quot;modestbranding&quot;: 1, &quot;rel&quot;: 0, &quot;iv_load_policy&quot;: 3}" data-thumbnail-file-name="sddefault" data-width="640">
<div class="play-button"></div>
<img loading="lazy" src="https://i.ytimg.com/vi/FpQ0yWA-oNQ/sddefault.jpg">
</div>
</div>
</div>
</section>
<footer class="fs-entry-footer">
<div class="fs-entry-credits collapsed">&nbsp;Credits</div>
<div class="fs-entry-meta collapsed">
<div class="submission-meta">
<div class="submission-meta__el1">
<div>Contributed by</div>
<div class="submission-meta__el2">
<div class="submission-meta__el5">
<a href="/user/Chris-Read/">
<img loading="lazy" class="submission-meta__avatar" title="Chris Read" src="/static/user_images/sr53041_2012711_175346639213.jpg" srcset="/static/user_images/sr53041_2012711_175346639213.jpg 1x, /static/user_images/r53041_2012711_175346639213.jpg 2x" alt="Chris Read" width="35" height="35">
</a>
</div>
<div class="submission-meta__el3">
<div>
<a href="/user/Chris-Read/">Chris Read</a> <span class="submission-meta__el7">• 11 months ago</span>
</div>
<div>
<b>151</b> Facts
</div>
</div>
</div>
</div>
<div class="submission-meta__el4">
<div class="submission-meta__el6">
This fact has been reviewed by a moderator
</div>
<a class="submission-meta__report" href="/contact/ask/?pt=3&amp;it=1&amp;fi=6024&amp;pf=Regarding: Nas's Represent fact (Fact ID: 6024)">⚑ Report wrong / missing information</a>
</div>
</div>
<div class="fs-references">
<span>References:</span>
<ol>
<li><a target="_blank" rel="noopener nofollow" href="https://youtu.be/FpQ0yWA-oNQ">https://youtu.be/FpQ0yWA-oNQ</a></li>
</ol>
</div>
<div class="fs-mod-credit">
</div>
</div>
</footer>
</div>
</section>
</article>
</div>
</section>
<div>
<p>Do you know an interesting fact or story about this track? <a href="/submit/?dest_track=Represent&amp;submission_type=F&amp;dest_artist=Nas">Submit it to us</a> and it will be shown here after review.</p>
<br>
<p>Check out the latest facts and stories submitted to the site <a href="/browse/facts/">here</a>.</p>
</div>
<section>
<header class="headTitle">
Credits<span class="betaBadge">Beta</span>
</header>
<div class="list bordered-list">
<div class="track-credit-wrapper">
<div class="track-credit-item">
<span class="track-credit-title">Composer:</span>&nbsp;
<span itemprop="contributor" itemscope="" itemtype="http://www.schema.org/Person">
<span itemprop="name"><a itemprop="url" href="/DJ-Premier/">DJ Premier</a></span>
</span>
</div>
<div class="track-credit-item">
<span class="track-credit-title">Lyricist:</span>&nbsp;
<span itemprop="contributor" itemscope="" itemtype="http://www.schema.org/Person">
<span itemprop="name"><a itemprop="url" href="/Nas/">Nas</a></span>
</span>
</div>
<div class="track-credit-item">
<span class="track-credit-title">Writers:</span>&nbsp;
<span itemprop="contributor" itemscope="" itemtype="http://www.schema.org/Person">
<span itemprop="name"><a itemprop="url" href="/DJ-Premier/">DJ Premier</a></span>
</span>
,&nbsp;
<span itemprop="contributor" itemscope="" itemtype="http://www.schema.org/Person">
<span itemprop="name"><a itemprop="url" href="/Nas/">Nas</a></span>
</span>
</div>
<div class="track-credit-item">
<span class="track-credit-title">Engineer:</span>&nbsp;
<span itemprop="contributor" itemscope="" itemtype="http://www.schema.org/Person">
<span itemprop="name"><a itemprop="url" href="/Eddie-Sancho/">Eddie Sancho</a></span>
</span>
</div>
</div>
</div>
</section>
<div style="margin-top: 1.5rem"></div>
<div class="ad-slot">
<div class="side-ad ">
<div id="cmn-feed-inline_-mid2">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['incontent', 'cmn-feed-inline_-mid2']]);
        </script>
<div class="commentsWrap">
<span class="headTitle">Discussion</span>
<p class="message">Be the first to comment on this track!</p>
<div class="commentInfo">
<p>You must be logged in to comment. Please <a href="/user/login/?next=/Nas/Represent/">sign in</a> or <a href="/user/registration/?next=/Nas/Represent/">sign up</a>.</p>
</div>
</div>
<div style="margin-top: 1.5rem"></div>
<div class="ad-slot">
<div class="side-ad ">
<div id="cmn-feed-inline_-bottom1">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['incontent', 'cmn-feed-inline_-bottom1']]);
        </script>
</div>
<div class="sidebar-container">
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-top">
<div id="cmn-aside_0">
</div>
</div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect_sidebar', 'cmn-aside_0']]);
        </script>
<p id="PrimisSidebarPlaceholder" style="width:0px;height:0px;"></p>
<div id="lazyload-primis-sidebar" width="100%"></div>
<div class="ad-slot">
<div class="side-ad side-ad--no-margin-bottom">
<div id="cmn-feed-inline_-side1">
</div>
 </div>
</div>
<script>
            window.catalyst.cmd.push('loadAds',[['rect', 'cmn-feed-inline_-side1']]);
        </script>
</div>
</div>
</div>
</main>
<footer id="footer" class="footer">
<div class="footerInner">
<div class="sections-wrapper">
<section class="footerAbout footer-section">
<span class="footer-title">About Us</span>
<ul>
<li><a href="/about/">About Us</a></li>
<li><a href="/faq/">FAQs</a></li>
<li><a href="/privacy/">Privacy Policy</a></li>
<li><a href="/terms/">Terms and Conditions</a></li>
</ul>
</section>
<section class="footerCommunity footer-section">
<span class="footer-title">Community</span>
<ul>
<li><a href="/forum/" id="forumFooterLink">Forum</a></li>
<li><a href="/browse/top_contributors/">Top Contributors</a></li>
<li><a href="/browse/facts/">Latest Facts and Stories</a></li>
<li><a href="/browse/latest_comments/">Latest Comments</a></li>
<li><a href="/browse/users/">Members</a></li>
</ul>
</section>
<section class="footerContact footer-section">
<span class="footer-title">Contact</span>
<ul>
<li><a href="/contact/ask/">Contact Us</a></li>
<li><a href="/jobs/">Jobs</a></li>
<li><a href="/copyright/">Copyright / DMCA</a></li>
</ul>
<ul class="social">
<li><a href="https://www.facebook.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M17.347 25.346v-9.09h2.55l.33-3.21h-2.88v-1.888c0-.71.47-.874.802-.874h2.03V7.167l-2.798-.01c-3.106 0-3.812 2.324-3.812 3.81v2.08h-1.796v3.21h1.796v9.09h3.777" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.twitter.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.25 10.486c-.682.303-1.418.508-2.19.6.788-.472 1.392-1.22 1.678-2.11-.738.437-1.555.754-2.423.925-.695-.74-1.687-1.203-2.783-1.203-2.107 0-3.815 1.707-3.815 3.813 0 .3.034.59.1.87-3.17-.16-5.982-1.677-7.86-3.985-.33.563-.518 1.218-.518 1.918 0 1.322.672 2.49 1.695 3.174-.625-.02-1.213-.19-1.727-.478v.048c0 1.847 1.316 3.39 3.058 3.74-.318.086-.656.134-1.004.134-.246 0-.484-.025-.716-.07.484 1.516 1.893 2.618 3.56 2.65-1.305 1.022-2.947 1.632-4.735 1.632-.307 0-.61-.018-.91-.053 1.69 1.083 3.693 1.715 5.847 1.715 7.016 0 10.852-5.812 10.852-10.852 0-.165-.004-.33-.012-.493.745-.538 1.392-1.21 1.902-1.974" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.youtube.com/whosampled" target="_blank" rel="noopener nofollow" title="WhoSampled on YouTube"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 257.567 262.185"><g transform="translate(-239 -327.79)"><ellipse style="isolation: auto; mix-blend-mode: normal; --darkreader-inline-color: #e8e6e3; --darkreader-inline-fill: #181a1b;" cx="367.784" cy="458.883" rx="128.784" ry="131.092" color="#000" overflow="visible" fill="#fff" fill-rule="evenodd" data-darkreader-inline-color="" data-darkreader-inline-fill=""></ellipse><path d="M450.057 419.717c-1.992-7.578-7.857-13.545-15.305-15.572-13.499-3.679-67.631-3.679-67.631-3.679s-54.132 0-67.632 3.68c-7.448 2.026-13.314 7.994-15.305 15.571-3.617 13.737-3.617 42.394-3.617 42.394s0 28.658 3.617 42.394c1.992 7.578 7.857 13.546 15.305 15.571 13.5 3.68 67.632 3.68 67.632 3.68s54.132 0 67.631-3.68c7.448-2.025 13.314-7.993 15.305-15.571 3.617-13.737 3.617-42.394 3.617-42.394s0-28.657-3.617-42.394" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M349.416 488.13l45.244-26.018-45.244-26.02v52.038z" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path></g></svg></a></li>
<li><a href="https://www.instagram.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M16 7.156c-2.4 0-2.703.01-3.646.053-.94.042-1.584.192-2.147.41-.582.226-1.075.53-1.566 1.02-.49.492-.793.985-1.02 1.567-.218.562-.368 1.205-.41 2.147-.044.943-.053 1.244-.053 3.646s.01 2.703.052 3.646c.042.942.192 1.585.41 2.147.227.582.53 1.075 1.02 1.567.492.49.985.794 1.567 1.02.563.218 1.206.368 2.147.41.943.044 1.245.054 3.646.054 2.403 0 2.704-.01 3.647-.053.94-.042 1.584-.192 2.146-.41.582-.226 1.076-.53 1.567-1.02.492-.492.795-.985 1.02-1.567.22-.562.368-1.205.41-2.147.044-.943.054-1.244.054-3.646s-.01-2.703-.053-3.646c-.042-.942-.19-1.585-.41-2.147-.225-.582-.528-1.075-1.02-1.567-.49-.49-.985-.794-1.567-1.02-.562-.218-1.205-.368-2.146-.41-.943-.044-1.244-.054-3.647-.054zm0 1.593c2.362 0 2.642.008 3.575.05.862.04 1.33.185 1.64.306.414.16.71.352 1.02.66.308.31.5.605.66 1.018.12.31.266.78.305 1.642.042.933.05 1.212.05 3.574s-.008 2.64-.05 3.574c-.04.862-.184 1.33-.305 1.642-.16.413-.352.708-.66 1.017-.31.31-.606.5-1.02.66-.31.123-.778.267-1.64.306-.933.04-1.213.05-3.575.05-2.36 0-2.64-.01-3.573-.05-.862-.04-1.33-.184-1.642-.306-.413-.16-.707-.352-1.017-.66-.31-.31-.502-.605-.662-1.018-.12-.312-.265-.78-.305-1.642-.04-.933-.05-1.212-.05-3.574s.01-2.64.05-3.574c.04-.862.185-1.33.306-1.642.16-.413.352-.708.662-1.017.31-.31.604-.5 1.017-.66.31-.122.78-.266 1.642-.306.933-.042 1.212-.05 3.573-.05" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M16 18.948c-1.627 0-2.948-1.32-2.948-2.948s1.32-2.948 2.948-2.948 2.95 1.32 2.95 2.948-1.322 2.948-2.95 2.948zm0-7.49c-2.507 0-4.54 2.034-4.54 4.542s2.033 4.542 4.54 4.542c2.51 0 4.542-2.034 4.542-4.542S18.51 11.458 16 11.458M21.783 11.28c0 .585-.475 1.06-1.062 1.06-.585 0-1.06-.475-1.06-1.06 0-.587.475-1.063 1.06-1.063.588 0 1.063.476 1.063 1.062" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
<li><a href="https://www.mixcloud.com/whosampled/" target="_blank" rel="noopener nofollow" title="WhoSampled on Mixcloud"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.000001" height="32" width="32"><path d="M32 16c0-8.837-7.163-16-16-16C7.164 0 0 7.163 0 16s7.164 16 16 16c8.837 0 16-7.163 16-16" fill="#fff" style="--darkreader-inline-fill: #e8e6e3;" data-darkreader-inline-fill=""></path><path d="M26.043 22.013c-.138 0-.278-.04-.403-.122-.333-.222-.422-.674-.198-1.007.67-1 1.024-2.17 1.024-3.386 0-1.216-.354-2.387-1.024-3.387-.224-.332-.135-.784.198-1.007.333-.223.784-.134 1.007.198.83 1.242 1.27 2.692 1.27 4.197 0 1.504-.44 2.955-1.27 4.195-.14.21-.37.32-.604.32" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path><path d="M23.967 20.835c-.14 0-.28-.04-.406-.125-.33-.225-.417-.677-.192-1.01.442-.65.675-1.413.675-2.203 0-.79-.234-1.552-.675-2.206-.225-.33-.138-.782.194-1.007.332-.225.783-.137 1.008.195.605.894.925 1.938.925 3.02 0 1.08-.32 2.124-.926 3.018-.14.207-.37.32-.603.32M19.875 19.284H9.957c-1.335 0-2.42-1.083-2.42-2.415 0-1.333 1.085-2.417 2.42-2.417.648 0 1.256.25 1.712.708.284.285.743.285 1.027 0 .283-.282.283-.742 0-1.026-.5-.5-1.115-.84-1.783-1.01.69-1.514 2.218-2.524 3.925-2.524 2.376 0 4.31 1.93 4.31 4.303 0 .462-.073.915-.216 1.347-.127.38.08.792.46.918.075.025.152.037.23.037.303 0 .586-.193.687-.498.096-.285.167-.577.215-.874.668.26 1.142.907 1.142 1.664 0 .985-.803 1.787-1.792 1.787zm.698-4.95c-.286-2.907-2.748-5.186-5.734-5.186-2.474 0-4.664 1.588-5.452 3.9-1.866.276-3.305 1.882-3.305 3.82 0 2.133 1.74 3.868 3.874 3.868h9.918c1.79 0 3.245-1.453 3.245-3.24 0-1.546-1.093-2.84-2.547-3.16" fill="#292827" style="--darkreader-inline-fill: #cfcbc4;" data-darkreader-inline-fill=""></path></svg></a></li>
</ul>
</section>
<section class="footerPartners footer-section">
<span class="footer-title">Partners</span>
<ul>
<li><a href="/metadata/" target="_blank" rel="noopener">Metadata / API</a></li>
<li><a href="/metadata/#customers" target="_blank" rel="noopener">Customers</a></li>
<li><a href="/apps/">App Gallery</a></li>
</ul>
</section>
<section class="footerSitemaps footer-section">
<span class="footer-title">Sitemaps</span>
<ul>
<li><a href="/sitemap/artist/A/">Artists</a></li>
<li><a href="/sitemap/track/A/">Tracks</a></li>
<li><a href="/sitemap/sample/A/">Samples</a></li>
<li><a href="/sitemap/cover/A/">Covers</a></li>
<li><a href="/sitemap/remix/A/">Remixes</a></li>
</ul>
</section>
</div>
<p class="footer-copyright">Copyright © 2022 WhoSampled.com Limited. All rights reserved.</p>
</div>
</footer>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="/static/js/main.js?512716070721"></script>
<script>
    var WS = WS || {};
    WS.voteFactURL = "/ajax/vote_fact/";
</script>
<script src="/static/js/embed/embed-lazyload.js?014613270521"></script>
<script src="/static/js/embed/unmanaged-youtube-player.js?171812230320"></script>
<script src="/static/js/facts/facts.js?534116170820"></script>
<script src="https://www.youtube.com/iframe_api" async=""></script>
<script>
  (function ($) {
    'use strict';

    var sessionID,
        sessionAge,
        sessionMaxAge = 86400 * 1000,
        now;

    if (!('localStorage' in window)) {
      return;
    }

    sessionID = localStorage.getItem('ws_session_id');
    sessionAge = localStorage.getItem('ws_session_age');

    if (sessionID !== null && sessionAge !== null) {
      sessionAge = parseInt(sessionAge, 10);
      now = (new Date()).getTime();

      if ((now - sessionAge) > sessionMaxAge) {
        sessionID = uuid();
        sessionAge = now;
        localStorage.setItem('ws_session_id', sessionID);
        localStorage.setItem('ws_session_age', sessionAge);
      }
    } else {
      sessionID = uuid();
      sessionAge = (new Date()).getTime();
      localStorage.setItem('ws_session_id', sessionID);
      localStorage.setItem('ws_session_age', sessionAge);
    }

    $.post("/ajax/hit/", {
      sid: sessionID,
      oid: "1226",
      ct: "12"
    });


    function uuid() {
      // UUID v4 generator (RFC4122 compliant).
      // Taken from https://gist.github.com/jcxplorer/823878
      var uuid = "", i, random;

      for (i = 0; i < 32; i++) {
        random = Math.random() * 16 | 0;

        if (i == 8 || i == 12 || i == 16 || i == 20) {
          uuid += "-";
        }

        uuid += (i == 12 ? 4 : (i == 16 ? (random & 3 | 8) : random)).toString(16);
      }

      return uuid;
    }

  }(jQuery));
</script>
<script>
      $('.top-menu-avatar').on('click touchstart', function (evt) {
        evt.preventDefault();
        evt.stopPropagation();
        $('#top-menu-dropdown').toggleClass('open');
      });

      $('#top-menu-dropdown, .downloadDropdown, .buyDropdown').on('click touchstart', function (evt) {
        evt.stopPropagation();
      });

      $('html').on('click touchstart', function () {
        $('.downloadDropdown, .buyDropdown').hide();
        $('#top-menu-dropdown').removeClass('open');
      });
    </script>
<script src="https://cdn.jsdelivr.net/npm/vanilla-lazyload@17.4.0/dist/lazyload.min.js"></script>
<script>
        function load_primis_sidebar() {
            if (!window.PrimisSidebarLoaded) {
                var mElmt, primisElmt = document.createElement('script');
                primisElmt.setAttribute('type', 'text/javascript');
                primisElmt.setAttribute('async','async');
                primisElmt.setAttribute('src', 'https://live.primis.tech/live/liveView.php?s=107513');
                mElmt = document.getElementById('PrimisSidebarPlaceholder');
                if (mElmt) {
                    mElmt.parentNode.insertBefore(primisElmt, mElmt.nextSibling);
                    mElmt.parentNode.removeChild(mElmt);
                }
                window.PrimisSidebarLoaded = true;
            }
        }

        var lazyLoadInstancePrimisSidebar = new LazyLoad({
            elements_selector: "#lazyload-primis-sidebar",
            callback_enter: load_primis_sidebar
        });
    </script>


</body>
"""