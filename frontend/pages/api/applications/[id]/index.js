export default async (req, res) => {
	try {
		// Get access token from authorization header
		const authHeader = req.headers.authorization
		if (!authHeader) {
			return res.status(401).json({ message: 'Authorization header missing' })
		}
		if (req.method === 'PUT') {
			// Get the application id from the query
			const { id } = req.query
			// Send a PUT request to the API to update the application status
			const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs/applications/${id}`, {
				method: 'PUT',
				headers: {
					Authorization: authHeader,
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(req.body)
			})
			const data = await response.json()
			if (response.ok) {
				return res.status(200).json(data)
			}
		} else {
			return res.status(405).json({ message: 'Method not allowed' })
		}
	} catch (error) {
		console.error('Error accessing api/jobs/[id]/apply', error)
		return res.status(403).json({ message: 'User forbidden' })
	}
}