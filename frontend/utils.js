/* Prettify job type */
export const prettifyJobType = (type) => {
	switch (type) {
		case 'full_time':
			return 'Full time'
		case 'part_time':
			return 'Part time'
		case 'contract':
			return 'Contract'
		case 'internship':
			return 'Internship'
	}
}

/* Add https to url if not present */
export const addHttps = (url) => {
	if (!url.startsWith('http')) {
		return `https://${url}`
	}
	return url
}

/* Format date to: Jul 24, 2021 at 1:50 PM */
export const formatDate = (date) => {
	return new Date(date).toLocaleString('en-US', {
		month: 'short',
		day: 'numeric',
		year: 'numeric',
		hour: 'numeric',
		minute: 'numeric',
		hour12: true,
	})
}