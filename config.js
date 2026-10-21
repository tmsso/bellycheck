// Belly Check site settings. Both values are public by design and safe to commit.
window.BELLY_CONFIG = {
  goatcounter: 'bellycheck', // GoatCounter site code, e.g. 'bellycheck' for https://bellycheck.goatcounter.com (visit stats + Thanks button)
  web3forms: '08f8b072-84e8-4620-a5b2-557f9f3e8484', // Web3Forms access key (feedback form; messages arrive by email)
};
(function (c) {
  if (!c.goatcounter) return;
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://gc.zgo.at/count.js';
  s.setAttribute('data-goatcounter', 'https://' + c.goatcounter + '.goatcounter.com/count');
  document.head.appendChild(s);
})(window.BELLY_CONFIG);
