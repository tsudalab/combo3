import numpy as np
from .. import inf


class model(object):
    ''' bayesian linear model '''
    def __init__(self, lik, prior, options={}):
        self.prior = prior
        self.lik = lik
        self.nbasis = self.lik.linear.basis.nbasis
        self._init_prior(prior)
        self._set_options(options)
        self.stats = ()

    def prepare(self, X, t, Psi=None):
        if self.method == 'exact':
            inf.exact.prepare(blm=self, X=X, t=t, Psi=Psi)
        else:
            pass

    def update_stats(self, x, t, psi=None):
        if self.method == 'exact':
            self.stats = inf.exact.update_stats(self, x, t, psi)
        else:
            pass

    def get_post_params_mean(self):
        if self.method == 'exact':
            self.lik.linear.params = inf.exact.get_post_params_mean(blm=self)

    def get_post_fmean(self, X, Psi=None, w=None):
        if self.method == 'exact':
            fmu = inf.exact.get_post_fmean(self, X, Psi, w)
        else:
            pass
        return fmu

    def sampling(self, w_mu=None, N=1, alpha=1.0):
        if self.method == 'exact':
            w_hat = inf.exact.sampling(self, w_mu, N, alpha=alpha)
        else:
            pass
        return w_hat

    def post_sampling(self, Xtest, Psi=None, N=1, alpha=1.0):
        if Psi is None:
            Psi = self.lik.get_basis(Xtest)
        w_hat = self.sampling(N=N, alpha=alpha)
        return Psi.dot(w_hat) + self.lik.linear.bias

    def predict_sampling(self, Xtest, Psi=None, N=1):
        fmean = self.post_sampling(Xtest, Psi, N=N)
        return fmean + np.sqrt(self.lik.cov.sigma2) \
            * np.random.randn(Xtest.shape[0], N)

    def get_post_fcov(self, X, Psi=None, diag=True):
        if self.method == 'exact':
            fcov = inf.exact.get_post_fcov(self, X, Psi, diag=True)
        else:
            pass
        return fcov

    def _set_options(self, options):
        self.method = options.get('method', 'exact')

    def _init_prior(self, prior):
        ''' initialize the prior distribution '''
        if prior is None:
            prior = prior.gauss(self.nbasis)
        self.prior = prior
