test = {
  'name': 'Question 04_very_actives',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'very_actives'
          >>> 'very_actives' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'very_actives'
          >>> # from its initial state (of ...)
          >>> very_actives is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(very_actives) == 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(very_actives >= 0)
          True
          >>> np.all(very_actives <= 74)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> 13.47 <= np.mean(very_actives) <= 14.06
          True
          >>> 2.6 <= np.std(very_actives) <= 3.06
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
