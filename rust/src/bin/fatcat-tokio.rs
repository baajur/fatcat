//! Main binary entry point for fatcat implementation.

#![allow(missing_docs)]

// Imports required by this file.
extern crate fatcat;
extern crate fatcat_api;
extern crate hyper;
extern crate swagger;
//extern crate openssl;
//extern crate native_tls;
extern crate tokio_proto;
//extern crate tokio_tls;
extern crate clap;

//use openssl::x509::X509_FILETYPE_PEM;
//use openssl::ssl::{SslAcceptorBuilder, SslMethod};
//use openssl::error::ErrorStack;
use clap::{App, Arg};
use hyper::server::Http;
use swagger::auth::AllowAllAuthenticator;
use tokio_proto::TcpServer;

// Builds an SSL implementation for Simple HTTPS from some hard-coded file names
/*
fn ssl() -> Result<SslAcceptorBuilder, ErrorStack> {
    let mut ssl = SslAcceptorBuilder::mozilla_intermediate_raw(SslMethod::tls())?;

    // Server authentication
    ssl.set_private_key_file("examples/server-key.pem", X509_FILETYPE_PEM)?;
    ssl.set_certificate_chain_file("examples/server-chain.pem")?;
    ssl.check_private_key()?;

    Ok(ssl)
}
*/

/// Create custom server, wire it to the autogenerated router,
/// and pass it to the web server.
fn main() {
    let matches = App::new("server")
        .arg(
            Arg::with_name("https")
                .long("https")
                .help("Whether to use HTTPS or not"),
        )
        .get_matches();

    let service_fn = fatcat_api::server::auth::NewService::new(AllowAllAuthenticator::new(
        fatcat::NewService,
        "cosmo",
    ));

    let addr = "127.0.0.1:8080"
        .parse()
        .expect("Failed to parse bind address");
    if matches.is_present("https") {
        unimplemented!()
    //let ssl = ssl().expect("Failed to load SSL keys");
    //let builder: native_tls::TlsAcceptorBuilder = native_tls::backend::openssl::TlsAcceptorBuilderExt::from_openssl(ssl);
    //let tls_acceptor = builder.build().expect("Failed to build TLS acceptor");
    //TcpServer::new(tokio_tls::proto::Server::new(Http::new(), tls_acceptor), addr).serve(service_fn);
    } else {
        // Using HTTP
        TcpServer::new(Http::new(), addr).serve(service_fn);
    }
}
