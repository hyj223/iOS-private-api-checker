Dropzone.autoDiscover = false;
var myDropzone = new Dropzone("#ipa_file", {
	url: "/ipa_post",
	maxFilesize: 1024,
	acceptedFiles: '.ipa',
	maxFiles: 5,
	success: function(d, data) {
		data = JSON.parse(data);
		if (data.success == 1) {
			//显示app信息
			$('#app_name').text(data.name);
			$('#app_version').text(data.version.originResult);
			$('#app_build_version').text(data.build_version.originResult);
			$('#bundle_identifier').text(data.bundle_id.originResult);
			$('#device_family').text(data.device_family.reviewResult);
			$('#ipa_filesize').text(data.ipa_filesize);
			$('#development_region').text(data.development_region.originResult);
			$('#target_os_version').text(data.tar_version.reviewResult);
			$('#minimum_os_version').text(data.min_version.reviewResult);
			//显示ipa的架构信息
			$('#app_arcs').text(data.arcs.originResult.join(' / '));
			$('#profile_type').text(data.profile_type.reviewResult);
			$('#expiration').text(data.expiration);
			//显示私有api信息
			$('#api_in_app div.api_section').remove();
			for (var i = 0; i < data.methods_in_app.length; i++) {
				var api = data.methods_in_app[i];
				var html = '<div class="api_section section__text mdl-cell mdl-cell--10-col-desktop mdl-cell--6-col-tablet mdl-cell--3-col-phone">' +
                  '<h5>' + (i + 1) + '、' + api.api_name + '</h5>' +
                  'api is ' + api.type + ', IN sdk ' + api.sdk + '、' + api.framework + ' -> ' + api.header_file + ' -> ' + api.class_name + ' -> '+ api.api_name +
                '</div>';
                $('#api_append_div').append(html);
			};
			$('#framework_in_app div.api_section').remove();
			for (var i = 0; i < data.private_framework.length; i++) {
				var framework = data.private_framework[i];
				var html = '<div class="api_section section__text mdl-cell mdl-cell--10-col-desktop mdl-cell--6-col-tablet mdl-cell--3-col-phone">' +
                  '<h5>' + (i + 1) + '、' + framework + '</h5>' +
                '</div>';
                $('#framework_append_div').append(html);
			};
		}
		else {
			alert(data.message);
		}
	}
});