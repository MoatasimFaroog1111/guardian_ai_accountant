import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App(){
  const [odoo,setOdoo]=useState(null); const [file,setFile]=useState(null); const [doc,setDoc]=useState(null); const [analysis,setAnalysis]=useState(null); const [status,setStatus]=useState('idle');
  useEffect(()=>{fetch(`${API}/api/odoo/status`).then(r=>r.json()).then(setOdoo).catch(()=>setOdoo({status:'api_unreachable'}));},[]);
  async function upload(){ if(!file) return; setStatus('uploading'); const fd=new FormData(); fd.append('file',file); const r=await fetch(`${API}/api/documents/upload`,{method:'POST',body:fd}); const j=await r.json(); setDoc(j); setStatus(j.status); }
  async function analyze(){ if(!doc) return; setStatus('analyzing'); const r=await fetch(`${API}/api/agent/analyze-document`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({document_id:doc.document_id})}); const j=await r.json(); setAnalysis(j); setStatus(j.validation?.status || 'analyzed'); }
  const valid=analysis?.validation?.is_valid;
  return <main><header><h1>Guardian AI Accountant</h1><p>Phase 1 foundation: upload, analyze, validate, approve later. No real Odoo posting.</p></header><section className="grid"><div className="card"><h2>Upload Document</h2><input type="file" onChange={e=>setFile(e.target.files[0])}/><button onClick={upload}>Upload Document</button><p>Status: <b>{status}</b></p></div><div className="card"><h2>Odoo Connection</h2><p>Status: <b>{odoo?.status || 'checking'}</b></p><p>Posting enabled: <b>{String(odoo?.posting_enabled ?? false)}</b></p></div><div className="card"><h2>Document Status</h2><pre>{JSON.stringify(doc,null,2)}</pre><button disabled={!doc} onClick={analyze}>Analyze</button></div><div className="card"><h2>Accounting Draft</h2><pre>{JSON.stringify(analysis,null,2)}</pre><button disabled={!valid}>Approve Draft</button><button onClick={()=>window.print()}>Export Report</button></div></section></main>;
}

createRoot(document.getElementById('root')).render(<App/>);
