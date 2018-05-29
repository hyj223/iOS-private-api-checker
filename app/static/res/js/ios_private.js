Dropzone.autoDiscover = false;
var myDropzone = new Dropzone("#ipa_file", {
	url: "/ipa_post",
	maxFilesize: 2048,
	acceptedFiles: '.ipa',
	maxFiles: 5,
	success: function(d, data) {
		data = JSON.parse(data);
		if (data.success == 1) {
			//显示app信息
			$('#app_name').text(data.name);
			// $('#app_version').text(version);
//			$('#app_build_version').text(data.build_version.originResult);
			// $('#bundle_identifier').text(data.bundle_id.originResult);
//			$('#device_family').text(data.device_family.reviewResult);
//			$('#ipa_filesize').text(data.ipa_filesize);
//			$('#development_region').text(data.development_region.originResult);
//			$('#target_os_version').text(data.tar_version.reviewResult);
//			$('#minimum_os_version').text(data.min_version.reviewResult);
			//显示ipa的架构信息
//			$('#app_arcs').text(data.arcs.originResult.join(' / '));
//			$('#profile_type').text(data.profile_type.reviewResult);
//			$('#expiration').text(data.expiration);
			//显示私有api信息
//			$('#api_in_app div.api_section').remove();
//			for (var i = 0; i < data.methods_in_app.length; i++) {
//				var api = data.methods_in_app[i];
//				var html = '<div class="api_section section__text mdl-cell mdl-cell--10-col-desktop mdl-cell--6-col-tablet mdl-cell--3-col-phone">' +
//                  '<h5>' + (i + 1) + '、' + api.api_name + '</h5>' +
//                  'api is ' + api.type + ', IN sdk ' + api.sdk + '、' + api.framework + ' -> ' + api.header_file + ' -> ' + api.class_name + ' -> '+ api.api_name +
//                '</div>';
//                $('#api_append_div').append(html);
//			};
			$("#checkInfoList tbody").html("");
			var checkListHTML = '';
			for (var i = 0; i < data.checkResult.length; i++) {
				var result = data.checkResult[i];
				console.log(result)
				var tr = '<tr><td>' + (i + 1) + '</td><td>' +  result.status + '</td><td>' + result.reviewItem + '</td><td>'
				  + result.originResult + '</td><td>' + result.reviewResult + '</td></tr>';
				// console.log(tr);
				checkListHTML += tr;
				// $('#checkInfoList tbody').append(tr);
				
				var versionStr = result['version'];
				if (typeof versionStr === "string") {
					$('#app_version').text(result.originResult);
				}

				var build_versionStr = result['build_version'];
				if (typeof build_versionStr === "string") {
					build_version = $('#app_version').text() + '(' + result.originResult + ')';
					$('#app_version').text(build_version)
				}

				var bundle_idStr = result['bundle_id'];
				if (typeof bundle_idStr === "string") {
					$('#bundle_identifier').text(result.originResult);
				}
				
			};
			$('#checkInfoList tbody').append(checkListHTML);
		}
		else {
			alert(data.message);
		}
	}
});