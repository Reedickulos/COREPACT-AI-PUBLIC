/**
 * Example: Public-safe JS client skeleton for a CORE PACT–style service.
 * No real endpoints or tokens are included. Replace placeholders with your own.
 */

const API_URL = process.env.COREPACT_API_URL || 'https://your-api.example.com/v1/demo';
const API_KEY = process.env.COREPACT_API_KEY || 'YOUR_API_KEY_HERE';

async function demoRequest(prompt) {
  const resp = await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({
      query: prompt,
      options: { temperature: 0.2 },
    }),
  });

  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Request failed: ${resp.status} ${text}`);
  }
  return await resp.json();
}

(async () => {
  try {
    const result = await demoRequest('Summarize the benefits of multi-agent collaboration.');
    console.log(JSON.stringify(result, null, 2));
  } catch (err) {
    console.error(err);
  }
})();

