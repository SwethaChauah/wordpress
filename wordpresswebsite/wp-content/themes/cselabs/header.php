<?php
/**
 * The header for our theme.
 *
 * Displays all of the <head> section and everything up till <div id="content">
 *
 * @package embr
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><?php wp_title( '|', true, 'right' ); ?></title>
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">

<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<div id="wrapper-one">
<div id="wrapper-two">
<div id="wrapper-three">
<div id="page" class="hfeed site">

	<a class="skip-link screen-reader-text" href="#content"><?php _e( 'Skip to content', 'embr' ); ?></a>

	<header id="masthead" class="site-header" role="banner">
    <div class="responsive-container">
		<div class="site-branding">
			<table width = "100%">
				<tr>
					<td>
						<div><img class="logo-image" src="/wordpresswebsite/wp-content/themes/embr/images/polylogo1.png"  /></div>
					</td>

						<td><input type ="search" size="12" placeholder="Quick search" style="position: relative; right: 0%; left: 480%; " />
					</td>
					<td><button type="button" size ="2"class="btn btn-lg btn-info" name = "login button" style="position: relative; right: 0%; left: 1230%;bottom: 10%; ">Login</button>
					</td>
				</tr>
			</table>
			<h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
			<h2 class="site-description"><?php bloginfo( 'description' ); ?></h2>

		</div>
<td><nav id="site-navigation" class="main-navigation" role="navigation">
							<?php wp_nav_menu( array( 'theme_location' => 'primary', 'menu_id' => 'main-nav' ) ); ?>
						</nav></td>	
					
			
							
					
		<!-- #site-navigation -->
	</div><!-- .responsive-container -->
    </header><!-- #masthead -->

	<?php
	
		if( get_theme_mod('embr_header_type', 'one') == 'one' ){
			get_template_part('slider', 'one');
		}else{
			get_template_part('custom', 'header');
		}
	
	?>
            
	<div id="content" class="site-content">
	<div class="responsive-container">