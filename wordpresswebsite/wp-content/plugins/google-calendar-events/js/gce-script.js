
/**
 * Public JS functions
 *
 * @package   GCE
 * @author    Phil Derksen <pderksen@gmail.com>, Nick Young <mycorpweb@gmail.com>
 * @license   GPL-2.0+
 * @copyright 2014 Phil Derksen
 */
(function($) {
	'use strict';

	$(function() {

		gce_tooltips($('.gce-has-events'));
		
		if( typeof gce_grid != 'undefined' ) {

			$('body').on( 'click', '.gce-change-month', function(e) {

				e.preventDefault();

				var navLink = $(this);

				var id = navLink.closest('.gce-calendar').parent().attr('id');

				//Extract month and year
				var month_year = navLink.attr('name').split('-', 2);
				var paging = navLink.attr('data-gce-grid-paging');

				//Add loading text to table caption
				$('#' + gce_grid[id].target_element + ' caption').html(gce.loadingText);
				//Send AJAX request
				$.post(gce.ajaxurl,{
					action:'gce_ajax',
					gce_type: gce_grid[id].type,
					gce_feed_ids: gce_grid[id].feed_ids,
					gce_title_text: gce_grid[id].title_text,
					gce_widget_id: gce_grid[id].target_element,
					gce_month: month_year[0],
					gce_year: month_year[1],
					gce_paging: paging,
					gce_nonce: gce.ajaxnonce
				}, function(data){
					//Replace existing data with returned AJAX data
					if(gce_grid[id].type == 'widget'){
						$('#' + gce_grid[id].target_element).html(data);
					}else{
						$('#' + gce_grid[id].target_element).replaceWith(data);
					}
					gce_tooltips($('#' + gce_grid[id].target_element + ' .gce-has-events'));
				});

				e.stopPropagation();
			});
		}

		$('body').on( 'click', '.gce-change-month-list', function(e) {

			e.preventDefault();

			var navLink = $(this);

			var start = navLink.parent().parent().parent().data('gce-start');
			var grouped = navLink.parent().parent().parent().data('gce-grouped');
			var title_text = navLink.parent().parent().parent().data('gce-title');
			var feed_ids = navLink.parent().parent().parent().data( 'gce-feeds');
			var sort = navLink.parent().parent().parent().data('gce-sort');
			var paging = navLink.parent().parent().parent().data('gce-paging');
			var paging_interval = navLink.parent().parent().parent().data('gce-paging-interval');
			var paging_direction = navLink.data('gce-paging-direction');
			var start_offset = navLink.parent().parent().parent().data('gce-start-offset');
			var paging_type = navLink.data('gce-paging-type');

			//Add loading text to table caption
			navLink.parent().parent().parent().find('.gce-month-title').html(gce.loadingText);

			//Send AJAX request
			$.post(gce.ajaxurl,{
				action:'gce_ajax_list',
				gce_feed_ids:feed_ids,
				gce_title_text:title_text,
				gce_start: start,
				gce_grouped: grouped,
				gce_sort: sort,
				gce_paging: paging,
				gce_paging_interval: paging_interval,
				gce_paging_direction: paging_direction,
				gce_start_offset: start_offset,
				gce_paging_type: paging_type,
				gce_nonce: gce.ajaxnonce
			}, function(data){
				navLink.parents('.gce-list').replaceWith(data);
			});

			e.stopPropagation();
		});

		function gce_tooltips(target_items) {

			target_items.each(function(){
				//Add qtip to all target items
				$(this).qtip({
					content: $(this).children('.gce-event-info'),
					position: { corner: { target: 'center', tooltip: 'bottomLeft' }, adjust: { screen: true } },
					hide: { fixed: true, delay: 100, effect: { length: 0 } },
					show: { solo: true, delay: 0, effect: { length: 0 } },
					style: { padding: "0", classes: { tooltip: 'gce-qtip', tip: 'gce-qtip-tip', title: 'gce-qtip-title', content: 'gce-qtip-content', active: 'gce-qtip-active' }, border: { width: 0 } }
				});
			});
		}
	});
}(jQuery))
