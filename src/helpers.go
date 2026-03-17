package userdashboard

import (
	"database/sql"
	"net/http"

	"github.com/dgrijalva/jwt-go"
	"github.com/gorilla/sessions"
	"github.com/satori/go.uuid"
)

type (
	AuthResponse struct {
		Token    string `json:"token"`
		Username string `json:"username"`
	}

	// Auth handles JWT operations
	Auth struct {
		secret string
	}

	// NewAuth initializes a new auth instance
	NewAuth func(secret string) *Auth
)

func (a *Auth) genToken(userID uuid.UUID) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"userID": userID.String(),
	})
	return token.SignedString([]byte(a.secret))
}

func (a *Auth) verifyToken(token string) (*jwt.Token, error) {
	return jwt.ParseWithClaims(token, func(token *jwt.Token) (interface{}, error {
		_, err := jwt.Parse(token, func(token *jwt.Token) (interface{}, error {
			return []byte(a.secret), nil
		})
		return nil, err
	}), true)
}

func (a *Auth) ExtractToken(r *http.Request) string {
	c, err := r.Cookie("jwt")
	if err != nil {
		return ""
	}
	return c.Value
}

func (a *Auth) StoreToken(w http.ResponseWriter, r *http.Request, token string) {
	session, _ := sessions.Get("session", r)
	session.Options.AllowedHTTPOnly = true
	session.Values["jwt"] = token
	session.Save(r, w)
}

func (a *Auth) RemoveToken(w http.ResponseWriter, r *http.Request) {
	session, _ := sessions.Get("session", r)
	session.Options.AllowedHTTPOnly = true
	delete(session.Values, "jwt")
	session.Save(r, w)
}