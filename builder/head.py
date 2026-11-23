# -*- coding: utf-8 -*-

def get_head_and_nav():
    return r'''<!doctype html>
<html lang="th" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CN 271 กลศาสตร์ของไหล ครบทุกบท · มหาวิทยาลัยธรรมศาสตร์</title>
  <meta name="description" content="สรุปสูตร ที่มา โจทย์ตัวอย่าง 74 ข้อ จุดดักข้อสอบ และแนวข้อสอบอัตนัยพร้อมเฉลยละเอียด 4 สเต็ป ครบทั้ง 5 บท และการวัดอัตราการไหล CN 271 วิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <link rel="stylesheet" href="assets/style.css?v=20261123">
  <script>
    (function(){
      var t = null;
      try { t = localStorage.getItem('theme'); } catch(e){}
      if (t !== 'light' && t !== 'dark') {
        t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      document.documentElement.setAttribute('data-theme', t);
    })();
  </script>
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="context-stroke"/>
    </marker>
  </defs>
</svg>

<nav class="toc" aria-label="สารบัญนำทาง">
  <a href="#sum" aria-current="page">สรุปภาพรวม</a>
  <a href="#ch1">บท 1 คุณสมบัติของไหล</a>
  <a href="#ch2">บท 2 สถิตยศาสตร์ &amp; ประตูน้ำ</a>
  <a href="#ch3">บท 3 จลนศาสตร์ &amp; โมเมนตัม</a>
  <a href="#ch4">บท 4 วิเคราะห์มิติ &amp; สเกล</a>
  <a href="#ch5">บท 5 ท่อส่งน้ำ &amp; วนลูป</a>
  <a href="#meter">เครื่องมือวัด &amp; Cavitation</a>
  <a href="#exam" class="gap">คลังข้อสอบ &amp; เก็งข้อสอบ</a>
  <a href="#calc" class="gap">คิดเลข</a>
  <a href="#ref">ตาราง &amp; คำศัพท์</a>
  <span class="sp"></span>
  <span class="tools">
    <button class="th" id="practice" type="button" aria-pressed="false" aria-label="โหมดฝึก ซ่อนวิธีทำ">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/></svg>
      <span class="lbl">ฝึก</span>
    </button>
    <button class="th" id="theme" type="button" aria-label="สลับโหมดสว่าง/มืด">
      <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>
      <span class="lbl" id="thl">โหมดมืด</span>
    </button>
  </span>
</nav>

<main>
<noscript><p style="padding:20px;color:red;text-align:center;">กรุณาเปิดการทำงานของ JavaScript เพื่อแสดงสูตรคณิตศาสตร์และใช้งานระบบ</p></noscript>
'''
