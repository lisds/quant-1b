test = {
  'name': '2.1.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(close_songs) >= {'Genre', 'Artist', 'like', 'love'}
          True
          >>> len(close_songs) == 7
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> titles = list(close_songs.index)
          >>> [title[:8] for title in titles]
          ['If This ', 'Big Red ', 'In the M', 'The Hard', 'One Time', 'This Tor', 'You Can ']
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
